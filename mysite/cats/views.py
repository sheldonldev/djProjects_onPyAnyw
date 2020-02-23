from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Breed, Cat


# Create your views here.

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        template = ""
        breed_count = Breed.objects.all().count()
        cat_count = Cat.objects.all().count()
        cat_list = Cat.objects.all()
        cxt = {
            'breed_count': breed_count,
            'cat_count': cat_count,
            'cat_list': cat_list,
        }
        return render(request, 'cats/cat_list.html', cxt)


class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        cat_count = Cat.objects.all().count()
        breed_count = Breed.objects.all().count()
        breed_list = Breed.objects.all()
        cxt = {
            'cat_count': cat_count,
            'breed_count': breed_count,
            'breed_list': breed_list,
        }
        return render(request, 'cats/breed_list.html', cxt)


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:index')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:index')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:index')


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:bread_list')


class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:bread_list')


class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:bread_list')

