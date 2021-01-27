from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.category.models import CategoryClub


class Club(models.Model):
    name = models.CharField(max_length=255, blank=False)
    type = models.ForeignKey(CategoryClub, related_name='clubs', on_delete=models.DO_NOTHING)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(max_length=14, blank=True, help_text=_('Contact phone number'))
    area = models.IntegerField()
    address = models.CharField(max_length=400, unique=True, blank=False)

    def __str__(self):
        return f'{self.type}-{self.name}'


class ClubImage(models.Model):
    club = models.ForeignKey(Club, related_name='images', on_delete=models.CASCADE)
    images = models.FileField(default='default_club_logo.jpg', upload_to='club_images', blank=True, null=True)
