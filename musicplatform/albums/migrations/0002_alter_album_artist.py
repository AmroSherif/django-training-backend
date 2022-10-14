# Generated by Django 4.1.2 on 2022-10-14 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("artists", "0001_initial"),
        ("albums", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="artist",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="artists.artist",
            ),
        ),
    ]
