from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_results', views.show_results),
]
