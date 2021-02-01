from django.urls import path

from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('blog/', blog_page, name='blog'),
    path('blog/<str:title>/', blog_detail, name='blog_detail'),   # we put a title as a slug
]