# Generated by Django 4.1.7 on 2023-06-27 05:28

import django.core.validators
from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.FileField(upload_to='images1080/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['gif', 'jpg', 'png', 'bmp', 'jp2']), gallery.models.file_validator]),
        ),
    ]