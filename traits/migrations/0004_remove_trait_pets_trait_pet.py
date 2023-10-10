# Generated by Django 4.2.6 on 2023-10-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0001_initial"),
        ("traits", "0003_alter_trait_pets"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trait",
            name="pets",
        ),
        migrations.AddField(
            model_name="trait",
            name="pet",
            field=models.ManyToManyField(related_name="traits", to="pets.pet"),
        ),
    ]
