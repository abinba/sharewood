# Generated by Django 2.2.2 on 2019-07-04 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20190704_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 4, 19, 28, 6, 500937)),
        ),
        migrations.AlterField(
            model_name='records',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 4, 19, 28, 6, 500486)),
        ),
    ]