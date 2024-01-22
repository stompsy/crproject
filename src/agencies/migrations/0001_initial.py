# Generated by Django 5.0.1 on 2024-01-21 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Agency",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("agency_name", models.CharField(max_length=100)),
                ("agency_description", models.TextField()),
                ("agency_url", models.URLField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="AgencyTypes",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("agency_type_name", models.CharField(max_length=100)),
                ("agency_type_description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "agency_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="agencies.agency",
                    ),
                ),
            ],
        ),
    ]