# Generated by Django 5.1.1 on 2024-09-08 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_kitchen_options_grill_ordering_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grill',
            options={'ordering': ('ordering',), 'verbose_name': 'Гриль', 'verbose_name_plural': 'Грили'},
        ),
    ]
