# Generated by Django 2.2.10 on 2020-10-27 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201024_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='review',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
