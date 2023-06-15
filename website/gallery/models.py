from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
    
class Images(models.Model):
    PICTURES = "PIC"
    MAPS = "MPS"
    YOUR_PICTURE = "YOP"
    GALLERY = [
        (PICTURES, "Picture"),
        (MAPS, "Map"),
        (YOUR_PICTURE, "Your picture"),
    ]
    gallery = models.CharField(
        max_length=3,
        choices=GALLERY,
        default=YOUR_PICTURE,
    )
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    
    def __str__(self):
        return self.gallery