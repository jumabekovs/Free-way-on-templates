from django.shortcuts import render

from apps.offer.models import Offer


def offers_page(request):
    offers = Offer.objects.all()
    return render(request, 'cards.html', locals())





