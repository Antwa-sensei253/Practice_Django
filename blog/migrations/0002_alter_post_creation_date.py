# Generated by Django 5.1.4 on 2024-12-18 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 18, 12, 16, 17, 956128, tzinfo=datetime.timezone.utc)),
        ),
    ]