# Generated by Django 2.2.10 on 2020-11-16 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20201116_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_make',
            field=models.DateField(verbose_name='Дата создания'),
        ),
    ]