# Generated by Django 2.2.12 on 2020-06-02 18:16

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=0, editable=False, populate_from='title', unique=True),
            preserve_default=False,
        ),
    ]