# Generated by Django 4.2.6 on 2023-10-09 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("groups", "0003_remove_group_pet"),
        ("pets", "0003_alter_pet_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="groups.group",
            ),
        ),
    ]
