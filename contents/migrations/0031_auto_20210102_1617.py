# Generated by Django 2.2.4 on 2021-01-02 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0030_auto_20201118_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='message',
            field=models.CharField(max_length=1000),
        ),
    ]