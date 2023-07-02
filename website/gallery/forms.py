from django import forms
from .models import Images
from django.core.files.uploadedfile import InMemoryUploadedFile



class ImageForm(forms.ModelForm):
    
    name = forms.CharField(label="ime", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Кратак опис фотографије коју намераваш да поставиш', 'aria-label':'Ime'}))
    image = forms.FileField(label="Slika", widget=forms.FileInput(attrs={'class':'form-control d-none', 'id':'inputGroupFile', 'accept':'.gif, .jpg, .png, .bmp, .jp2'}))
    class Meta:
        model = Images
        fields = ['name', 'image',]


