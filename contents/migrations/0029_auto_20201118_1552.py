# Generated by Django 2.2.4 on 2020-11-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0028_auto_20201118_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='focus',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
