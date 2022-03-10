from django.urls import path

from . import views


urlpatterns = [
    path('wall/', views.get_all_twits, name='twits')
]
