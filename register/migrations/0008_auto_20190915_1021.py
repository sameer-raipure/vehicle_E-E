# Generated by Django 2.1.5 on 2019-09-15 04:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20190915_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fac',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 15, 10, 21, 0, 27374)),
        ),
    ]