from django.urls import path, reverse_lazy

from . import views

app_name = 'ads'
urlpatterns = [
    path('', views.AdListView.as_view(), name='index'),
    path('ad/<int:pk>/', views.AdDetailView.as_view(), name='detail'),
    path('ad/create/', views.AdCreateView.as_view(), name='create'),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view(), name='update'),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view(), name='delete'),
]