# Generated by Django 4.1.2 on 2022-11-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_remove_extendeduser_repeated_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="extendeduser",
            name="password",
            field=models.CharField(max_length=256),
        ),
    ]
