# Generated by Django 3.2 on 2022-02-10 16:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20220210_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 2, 10, 16, 13, 39, 56768, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2022, 2, 10, 16, 13, 39, 56768, tzinfo=utc)),
        ),
    ]
