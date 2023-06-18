from django.db import models
import PIL 
from PIL import Image

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
    name = models.CharField(max_length=200, null=True, blank=True, default='picture')
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    image300 = models.ImageField(upload_to="images/%Y/%m/%d/", null=True,  blank=True, default='settings.MEDIA_ROOT/picture.jpg')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.gallery
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        widthCheck = img.width - img.height
        if img.width > 1080:
            baseWidth = 1080
            wPercent = (baseWidth/float(img.size[0]))
            hSize = int((float(img.size[1])*float(wPercent)))
            img = img.resize((baseWidth,hSize), Image.Resampling.LANCZOS)
            img.save(self.image.path)
            
        if widthCheck >= 0:
            baseWidth = 300
            wPercent = (baseWidth/float(img.size[0]))
            hSize = int((float(img.size[1])*float(wPercent)))
            img = img.resize((baseWidth,hSize), Image.Resampling.LANCZOS)
            img.save(self.image300.path)
        
        else:
            new_height = 300
            new_width  = int(new_height * img.width / img.height)
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            img.save(self.image300.path)
            