from django import forms
from .models import Chapter, Comment, Image
from django.core.files.uploadedfile import InMemoryUploadedFile


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['name', 'text']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['chapter', 'imageInSett']


class CommentForm(forms.ModelForm):
    name = forms.CharField(label="Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    text = forms.CharField(label="Text", max_length=1000, widget=forms.Textarea(attrs={'class':'form-control', 'rows':'2', 'placeholder':'Text'}))
    image = forms.ImageField(required=False, label="Picture", widget=forms.FileInput(attrs={'class':'form-control text-bg-primary border border-primary', 'placeholder':'Text'}))
    class Meta:
        model = Comment
        fields = ['name', 'text', 'image']
