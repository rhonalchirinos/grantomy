# Generated by Django 3.2.18 on 2023-03-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grantomy', '0003_zeus_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zeus',
            name='edad',
            field=models.IntegerField(default=None),
        ),
    ]
