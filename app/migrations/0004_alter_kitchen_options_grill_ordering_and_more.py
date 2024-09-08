# Generated by Django 5.1.1 on 2024-09-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_grill_photo_1_kitchen_photo_1_kitchen_photo_2_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kitchen',
            options={'ordering': ('ordering',), 'verbose_name': 'Кухня', 'verbose_name_plural': 'Кухни'},
        ),
        migrations.AddField(
            model_name='grill',
            name='ordering',
            field=models.SmallIntegerField(default=1, verbose_name='Порядок сортировки'),
        ),
        migrations.AlterField(
            model_name='grill',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='media/grill', verbose_name='Изображение №1'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='media/kitchen', verbose_name='Изображение №1'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='media/kitchen', verbose_name='Изображение №2'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='media/kitchen', verbose_name='Изображение №3'),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='photo_4',
            field=models.ImageField(blank=True, null=True, upload_to='media/kitchen', verbose_name='Изображение №4'),
        ),
    ]
