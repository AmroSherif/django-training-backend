# Generated by Django 4.1.2 on 2022-10-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0005_album_is_approved"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="is_approved",
            field=models.BooleanField(
                default=False,
                help_text=" Approve the album if its name is not explicit",
            ),
        ),
    ]
