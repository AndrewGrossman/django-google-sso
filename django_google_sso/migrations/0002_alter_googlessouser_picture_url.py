# Generated by Django 3.2 on 2022-10-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_google_sso", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="googlessouser",
            name="picture_url",
            field=models.URLField(max_length=2000),
        ),
    ]
