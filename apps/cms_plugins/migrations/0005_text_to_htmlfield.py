# Generated by Django 3.0.8 on 2020-09-22 07:16

import djangocms_text_ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cms_plugins", "0004_delete_contactpluginmodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="textimagepluginmodel",
            name="text",
            field=djangocms_text_ckeditor.fields.HTMLField(blank=True),
        ),
    ]