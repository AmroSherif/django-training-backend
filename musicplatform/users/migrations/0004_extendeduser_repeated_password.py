# Generated by Django 4.1.2 on 2022-11-03 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_extendeduser_bio"),
    ]

    operations = [
        migrations.AddField(
            model_name="extendeduser",
            name="repeated_password",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
