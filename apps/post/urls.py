from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', contact, name=contact),
    # path('blog/<str:title>/', PostDetailView.as_view(), name='blog_detail'),   # we put a title as a slug
    # path('add-post/', add_post, name='add_post'),
    # path('category/<str:slug>/', CategoryDetailView.as_view(), name='post_category')
]