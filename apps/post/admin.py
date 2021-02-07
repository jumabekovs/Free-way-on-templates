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


class ExtendPostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = ExtendPost
        fields = '__all__'


class ExtendPostAdmin(admin.ModelAdmin):
    form = ExtendPostAdminForm


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(ExtendPost, ExtendPostAdmin)
