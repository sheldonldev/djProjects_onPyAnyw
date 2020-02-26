from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.humanize.templatetags.humanize import naturaltime

from .owner import OwnerListView, OwnerDetailView, OwnerDeleteView
from .form import CreateForm, CommentForm
from .models import Ad, Comment, Favorite
from .utils import dump_queries


class AdListView(OwnerListView):
    model = Ad
    template_name = 'ads/ad_list.html'

    def get(self, request):
        # ad_list = Ad.objects.all().order_by('-updated_at')

        favorites = list()
        if request.user.is_authenticated:
            # rows = [{'id': 2}, {'id': 4} ... ]  (A list of rows)
            rows = request.user.favorite_ads.values('id')
            favorites = [row['id'] for row in rows]

        str_val = request.GET.get("search", False)
        if str_val:
            # # Simple title-only search
            # objects = Post.objects.filter(title__contains=str_val).select_related().order_by('-updated_at')[:10]

            # Multi-field search
            query = Q(title__contains=str_val)
            query.add(Q(text__contains=str_val), Q.OR)
            ad_list = Ad.objects.filter(query).select_related().order_by('-updated_at')[:]
        else:
            # try both versions with > 4 posts and watch the queries that happen
            ad_list = Ad.objects.all().order_by('-updated_at')[:]
            # objects = Ad.objects.select_related().all().order_by('-updated_at')[:]
        for ad in ad_list:
            ad.natural_created = naturaltime(ad.created_at)
            ad.natural_updated = naturaltime(ad.updated_at)
            if len(ad.text) > 50:
                ad.text_preview = ad.text[:50] + '...'
            else:
                ad.text_preview = ad.text

        ctx = {
            "ad_list": ad_list,
            "favorites": favorites,
            "search": str_val,
        }
        # dump_queries()    # check SQL queries
        return render(request, self.template_name, ctx)


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'

    def get(self, request, pk):
        ad = Ad.objects.get(id=pk)

        comments = Comment.objects.filter(ad=ad).order_by('-updated_at')
        comment_form = CommentForm()

        favorites = list()
        if request.user.is_authenticated:
            rows = request.user.favorite_ads.values('id')
            favorites = [row['id'] for row in rows]

        ctx = {
            'ad': ad,
            'comments': comments,
            'comment_form': comment_form,
            'favorites': favorites,
        }
        return render(request, self.template_name, ctx)


class AdCreateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:index')

    def get(self, request):
        form = CreateForm()
        ctx = {
            'form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = CreateForm(request.POST, request.FILES or None)
        if not form.is_valid():
            ctx = {
                'form': form,
            }
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        ad = form.save(commit=False)
        ad.owner = self.request.user
        ad.save()
        return redirect(self.success_url)


class AdUpdateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:index')

    def get(self, request, pk):
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=ad)
        ctx = {
            'form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=ad)
        if not form.is_valid():
            ctx = {
                'form': form,
            }
            return render(request, self.template_name, ctx)

        ad = form.save(commit=False)
        ad.save()
        return redirect(self.success_url)


class AdDeleteView(OwnerDeleteView):
    model = Ad
    template_name = 'ads/ad_confirm_delete.html'
    success_url = reverse_lazy('ads:index')


def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad=ad)
        comment.save()
        return redirect(reverse('ads:detail', args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_confirm_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        ad = self.object.ad
        return reverse('ads:detail', args=[ad.id])


# csrf exemption in class based views
# https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError


@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        print("Add PK", pk)
        title = get_object_or_404(Ad, id=pk)
        try:
            Favorite(user=request.user, ad=title).save()  # In case of duplicate key
        except IntegrityError as e:
            pass
        return HttpResponse()


@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        print("Delete PK", pk)
        title = get_object_or_404(Ad, id=pk)
        try:
            Favorite.objects.get(user=request.user, ad=title).delete()
        except Favorite.DoesNotExist as e:
            pass
        return HttpResponse()
