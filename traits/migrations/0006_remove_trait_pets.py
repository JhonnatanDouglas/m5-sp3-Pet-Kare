# Generated by Django 4.2.6 on 2023-10-09 17:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("traits", "0005_rename_pet_trait_pets"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trait",
            name="pets",
        ),
    ]
