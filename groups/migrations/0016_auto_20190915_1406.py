# Generated by Django 2.1.5 on 2019-09-15 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0015_auto_20190915_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 15, 14, 6, 14, 520119)),
        ),
    ]