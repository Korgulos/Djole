# Generated by Django 4.1.7 on 2023-06-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gallery", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="images",
            name="image300",
            field=models.ImageField(null=True, upload_to="images/%Y/%m/%d/"),
        ),
        migrations.AddField(
            model_name="images",
            name="name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
