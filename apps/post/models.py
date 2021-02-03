from django.db import models
from apps.category.models import CategoryPost


class Post(models.Model):
    title = models.ForeignKey(CategoryPost, related_name='posts', on_delete=models.DO_NOTHING)
    sub_title = models.CharField(max_length=100)
    image = models.ImageField(max_length=1000, upload_to='post_images', blank=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{self.sub_title}'


class ExtendPost(models.Model):
    post = models.ForeignKey(Post, related_name='extending_post', on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    text = models.TextField()
    images = models.ImageField(upload_to='post_images', blank=True)

    def __str__(self):
        return f'{self.header}'



