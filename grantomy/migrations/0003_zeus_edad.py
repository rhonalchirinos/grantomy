# Generated by Django 3.2.18 on 2023-03-27 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grantomy', '0002_auto_20230327_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='zeus',
            name='edad',
            field=models.IntegerField(default=1),
        ),
    ]
