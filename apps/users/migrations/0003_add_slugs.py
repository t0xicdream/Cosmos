# Generated by Django 3.0.8 on 2020-10-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_text_to_htmlfield"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="slug",
            field=models.CharField(default="None", max_length=20),
        ),
        migrations.AddField(
            model_name="committee",
            name="slug",
            field=models.CharField(default="None", max_length=20),
        ),
    ]
