# Generated by Django 2.2.2 on 2019-07-04 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20190630_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='comments_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 4, 13, 50, 42, 71193)),
        ),
        migrations.AlterField(
            model_name='records',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 4, 13, 50, 42, 70745)),
        ),
    ]
