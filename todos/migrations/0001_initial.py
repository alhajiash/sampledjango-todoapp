# Generated by Django 2.0.5 on 2018-05-27 09:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 27, 9, 34, 47, 195537, tzinfo=utc))),
            ],
        ),
    ]
