from django.shortcuts import render

from apps.category.models import CategoryClub
from apps.club.models import Club, ClubImage


def club_categories(request, name):  # this function requires the name of a category
    club_category = CategoryClub.objects.get(name=name)
    club_type = Club.objects.filter(type=name)  # Club model has type that is slug in category
    return render(request, 'club_category.html', locals())


def club_detail(request, name):
    club_name = Club.objects.get(name=name)
    club_images = ClubImage.objects.filter()     # id required
    return render(request, 'club_detail.html', locals())

