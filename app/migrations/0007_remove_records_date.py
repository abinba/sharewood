# Generated by Django 2.2.2 on 2019-06-18 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190618_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='date',
        ),
    ]
