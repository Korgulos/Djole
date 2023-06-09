# Generated by Django 4.1.7 on 2023-04-20 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Chapter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=60)),
                ("text", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="OldCountry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "imageInSett",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "chapter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="index.chapter"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=60)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("text", models.TextField()),
                (
                    "chapter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="index.chapter"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="chapter",
            name="oldCountry",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="index.oldcountry"
            ),
        ),
    ]
