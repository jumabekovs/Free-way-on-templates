from django.contrib import admin
from .models import Post, ExtendPost
from django.contrib.gis import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class CommentAdmin(admin.TabularInline):
    model = ExtendPost
    max_num = 1
    extra = 3


class PostAdmin(admin.ModelAdmin):
    form = NewAdminForm
    inlines = [CommentAdmin, ]


admin.site.register(Post, PostAdmin)
