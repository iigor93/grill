# Generated by Django 5.1.1 on 2024-09-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_grill'),
    ]

    operations = [
        migrations.AddField(
            model_name='grill',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение №1'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение №1'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение №2'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение №3'),
        ),
        migrations.AddField(
            model_name='kitchen',
            name='photo_4',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение №4'),
        ),
    ]
