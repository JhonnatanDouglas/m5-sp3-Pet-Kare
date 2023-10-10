# Generated by Django 4.2.6 on 2023-10-06 20:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pet",
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
                ("name", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("weight", models.FloatField()),
                (
                    "sex",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Not Informed", "Not Informed"),
                        ],
                        default="Not Informed",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
