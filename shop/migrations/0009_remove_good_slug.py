# Generated by Django 2.2.10 on 2020-10-19 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20201019_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='slug',
        ),
    ]
