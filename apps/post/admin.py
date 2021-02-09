from django.contrib import admin
from .models import Post, ExtendPost
from django.contrib.gis import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    list_filter = ('title', )

    class Meta:
        model = Post
        fields = '__all__'


class ExtendPostInline(admin.TabularInline):
    model = ExtendPost
    max_num = 5
    extra = 2


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    inlines = [ExtendPostInline, ]


admin.site.register(Post, PostAdmin)
