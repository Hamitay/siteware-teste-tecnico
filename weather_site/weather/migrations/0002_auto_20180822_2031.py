# Generated by Django 2.0.6 on 2018-08-22 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='city',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]