# Generated by Django 3.2 on 2022-02-10 14:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 14, 19, 53, 881147, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 14, 19, 53, 881147, tzinfo=utc)),
        ),
    ]
