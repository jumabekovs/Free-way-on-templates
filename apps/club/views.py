from django.shortcuts import render

from apps.category.models import CategoryClub
from apps.club.models import Club, ClubImage


def club_categories(request, name):  # this function requires the name of a category
    club_category = CategoryClub.objects.get(slug=name)
    club_type = Club.objects.filter(type=name)  # Club model has type that is slug in category
    return render(request, 'club_category.html', locals())


def club_detail(request, name):
    club_name = Club.objects.get(name=name)
    images = club_name.images.all()  # getting all images of a particular club
    return render(request, 'club_detail.html', locals())

