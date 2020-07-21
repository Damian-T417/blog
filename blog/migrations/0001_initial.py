# Generated by Django 2.2.12 on 2020-06-02 18:14

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('draft', models.BooleanField(default=True)),
                ('publish_date', models.DateField()),
                ('tags', models.ManyToManyField(to='blog.Tag')),
            ],
        ),
    ]
