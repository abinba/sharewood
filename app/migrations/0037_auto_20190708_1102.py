# Generated by Django 2.2.2 on 2019-07-08 11:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_auto_20190706_1853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'Материал', 'verbose_name_plural': 'Материалы'},
        ),
        migrations.AlterModelOptions(
            name='records',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.RemoveField(
            model_name='records',
            name='media',
        ),
        migrations.AddField(
            model_name='media',
            name='part_num',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='media',
            name='record',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Records'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 8, 11, 2, 2, 452020)),
        ),
        migrations.AlterField(
            model_name='media',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='records',
            name='author',
            field=models.CharField(default='arcturus5340', max_length=60),
        ),
        migrations.AlterField(
            model_name='records',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 8, 11, 2, 2, 450899)),
        ),
        migrations.AlterField(
            model_name='records',
            name='description',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='records',
            name='includes',
            field=models.TextField(default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='records',
            name='main_pic',
            field=models.FileField(upload_to='static/record_src/'),
        ),
        migrations.AlterField(
            model_name='records',
            name='pre_video',
            field=models.FileField(upload_to='static/record_src/'),
        ),
        migrations.AlterField(
            model_name='records',
            name='tags',
            field=models.TextField(default='code, #ihatejs, abinba!', max_length=255),
        ),
        migrations.AlterField(
            model_name='records',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]