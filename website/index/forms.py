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
    class Meta:
        model = Comment
        fields = ['name', 'text', 'image', 'chapter'] 