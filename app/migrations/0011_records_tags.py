# Generated by Django 2.2.2 on 2019-06-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_records_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='tags',
            field=models.TextField(default='code, #ihatejs, abinba!'),
        ),
    ]
