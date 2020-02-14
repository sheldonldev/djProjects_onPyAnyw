from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'hello'
urlpatterns = [
    path('', TemplateView.as_view(template_name='hello/index.html'), name='index'),

    path('cookies', views.cookie, name='cookie'),
    path('visit_counter', views.visit_counter, name='visit_counter'),
]