from django.urls import path

from .views import *

urlpatterns = [
    path('cards/', offers_page, name='cards'),

]

