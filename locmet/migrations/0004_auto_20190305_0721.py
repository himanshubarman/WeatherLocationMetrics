# Generated by Django 2.1.7 on 2019-03-05 07:21

from django.db import migrations, models
import locmet.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locmet', '0003_auto_20190305_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rainfall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('year', models.IntegerField(validators=[locmet.models.BaseMetrics.year_validation])),
                ('month', models.IntegerField(choices=[(1, 'Jan'), (2, 'Feb'), (3, 'Mar'), (4, 'Apr'), (5, 'May'), (6, 'Jun'), (7, 'Jul'), (8, 'Aug'), (9, 'Sept'), (10, 'Oct'), (11, 'Nov'), (12, 'Dec')])),
                ('location', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tmax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('year', models.IntegerField(validators=[locmet.models.BaseMetrics.year_validation])),
                ('month', models.IntegerField(choices=[(1, 'Jan'), (2, 'Feb'), (3, 'Mar'), (4, 'Apr'), (5, 'May'), (6, 'Jun'), (7, 'Jul'), (8, 'Aug'), (9, 'Sept'), (10, 'Oct'), (11, 'Nov'), (12, 'Dec')])),
                ('location', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('year', models.IntegerField(validators=[locmet.models.BaseMetrics.year_validation])),
                ('month', models.IntegerField(choices=[(1, 'Jan'), (2, 'Feb'), (3, 'Mar'), (4, 'Apr'), (5, 'May'), (6, 'Jun'), (7, 'Jul'), (8, 'Aug'), (9, 'Sept'), (10, 'Oct'), (11, 'Nov'), (12, 'Dec')])),
                ('location', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='tmin',
            unique_together={('location', 'year', 'month')},
        ),
        migrations.AlterUniqueTogether(
            name='tmax',
            unique_together={('location', 'year', 'month')},
        ),
        migrations.AlterUniqueTogether(
            name='rainfall',
            unique_together={('location', 'year', 'month')},
        ),
    ]