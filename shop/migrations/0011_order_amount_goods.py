# Generated by Django 2.2.10 on 2020-11-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20201115_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount_goods',
            field=models.IntegerField(default=1),
        ),
    ]
