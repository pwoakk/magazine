# Generated by Django 3.2 on 2022-02-10 14:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20220210_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 14, 23, 21, 592465, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 14, 23, 21, 592465, tzinfo=utc)),
        ),
    ]