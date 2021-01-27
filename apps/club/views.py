from django.shortcuts import render

from apps.category.models import CategoryClub
from apps.club.models import Club


def club_categories(request, name):
    club_category = CategoryClub.objects.get(name=name)
    clubs = Club.objects.filter(type=name)
    return render(request, 'club_category.html', {'club_category': club_category, 'clubs': clubs})
