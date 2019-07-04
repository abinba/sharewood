# Generated by Django 2.2.2 on 2019-06-27 17:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20190627_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='record_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 27, 17, 28, 44, 177594)),
        ),
        migrations.AlterField(
            model_name='records',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 27, 17, 28, 44, 177164, tzinfo=utc)),
        ),
    ]