# Generated by Django 3.1 on 2020-08-05 02:39

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RelatedData",
            fields=[
                (
                    "id",
                    models.CharField(max_length=32, primary_key=True, serialize=False),
                ),
                ("extra_data", models.TextField(blank=True, default="")),
            ],
        ),
        migrations.AlterField(
            model_name="comment",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="poll",
            name="pub_date",
            field=models.DateTimeField(verbose_name="date published"),
        ),
    ]
