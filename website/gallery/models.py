from django.db import models
from PIL import Image
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
import magic

# Create your models here.
    
custom_validator = FileExtensionValidator(['gif', 'jpg', 'png', 'bmp', 'jp2'])

def file_validator(file):
    accept = ['image/png', 'image/jpeg', 'image/gif', 'image/x-ms-bmp']
    file_type = magic.from_buffer(file.read(1024), mime=True)
    if file_type not in accept:
        raise ValidationError("Nije validan fajl")
        
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
    approved = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True, blank=True, default='picture')
    image = models.FileField(upload_to="images1080/%Y/%m/%d/", validators=[custom_validator, file_validator] )
    image300 = models.ImageField(upload_to="images300/%Y/%m/%d/", null=True,  blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
       
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
                       
    def delete(self):
        try:
            self.image.delete()
            self.image300.delete()
        except:
            print("Images {} and {}".format(self.image, self.image300))
        super().delete()