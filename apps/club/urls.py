from django.urls import path

from .views import club_categories

urlpatterns = [
    path('<str:name>/', club_categories, name='club-category')
]