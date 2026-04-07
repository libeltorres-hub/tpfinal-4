from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Page


class PageForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget(), label='Descripción')

    class Meta:
        model = Page
        fields = ['title', 'subtitle', 'body', 'image']
