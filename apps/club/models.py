from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.category.models import CategoryClub

GENDER_SEGREGATION = (
    ('men', _('Only for Men ')),
    ('women', _('Only for Women')),
    ('both', _('Open')),
)


class ClubImage(models.Model):
    images = models.FileField(default='default_club_logo.jpg', upload_to='club_images', blank=True, null=True)


class Club(models.Model):
    name = models.CharField(max_length=255, blank=False)
    type = models.ForeignKey(CategoryClub, related_name='club_types', on_delete=models.DO_NOTHING)
    gender_segregation = models.CharField(max_length=25, choices=GENDER_SEGREGATION)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(max_length=14, blank=True, help_text=_('Contact phone number'))
    area = models.IntegerField()
    address = models.CharField(max_length=400, unique=True, blank=False)
    image = models.ForeignKey(ClubImage, related_name='club', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.type}-{self.name}'

    @property
    def image_url(self):
        if self.images and hasattr(self.images, 'url'):
            return self.images.url

