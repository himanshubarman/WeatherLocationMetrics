# Generated by Django 2.1.7 on 2019-03-05 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locmet', '0002_auto_20190228_1226'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rainfall',
        ),
        migrations.DeleteModel(
            name='Tmax',
        ),
        migrations.DeleteModel(
            name='Tmin',
        ),
    ]
