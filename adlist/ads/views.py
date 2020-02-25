from django.shortcuts import render
from django.views import View
from django.views import generic
from django.urls import reverse_lazy

from .owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .models import Ad


class AdListView(OwnerListView):
    model = Ad
    template_name = 'ads/ad_list.html'


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:index')


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:index')


class AdDeleteView(OwnerDeleteView):
    model = Ad
    template_name = 'ads/ad_confirm_delete.html'
    success_url = reverse_lazy('ads:index')
