# Generated by Django 2.2.2 on 2019-06-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_records_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='audio',
            field=models.FileField(default='/static/record_src/r1/media/01. Balls To The Wall.mp3', upload_to=''),
        ),
    ]