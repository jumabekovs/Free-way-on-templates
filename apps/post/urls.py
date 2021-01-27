from django.urls import path

from .views import home_page

urlpatterns = [
    path('', home_page, name='home'),
    path('blog/', home_page, name='home'),
]