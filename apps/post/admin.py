from django.contrib import admin
from .models import Post, ExtendPost


class CommentAdmin(admin.TabularInline):
    model = ExtendPost
    max_num = 5
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentAdmin, ]


admin.site.register(Post, PostAdmin)
