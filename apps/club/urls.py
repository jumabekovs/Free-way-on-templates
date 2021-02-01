from django.urls import path

from .views import *

urlpatterns = [
    path('type/<str:name>/', club_categories, name='club-category'),
    path('name/<str:name>/', club_detail, name='club_detail'),
]