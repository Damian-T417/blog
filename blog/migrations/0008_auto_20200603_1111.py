# Generated by Django 2.2.12 on 2020-06-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200603_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='blog/uploads/', verbose_name='Imagen'),
        ),
    ]