# Generated by Django 2.2.2 on 2019-07-09 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_auto_20190709_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='revenue',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 9, 8, 47, 35, 567805)),
        ),
        migrations.AddField(
            model_name='revenue',
            name='income',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 9, 8, 47, 35, 567481)),
        ),
        migrations.AlterField(
            model_name='records',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 9, 8, 47, 35, 565928)),
        ),
    ]
