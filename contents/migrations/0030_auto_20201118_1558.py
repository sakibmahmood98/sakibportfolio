# Generated by Django 2.2.4 on 2020-11-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0029_auto_20201118_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='summary',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='seminar',
            name='summary',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]