# Generated by Django 3.2 on 2022-02-11 10:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20220211_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 11, 10, 12, 19, 505238, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 11, 10, 12, 19, 505238, tzinfo=utc)),
        ),
    ]
