# Generated by Django 3.2.18 on 2023-03-28 17:47

from django.db import migrations, models
import pretix.base.models.items


class Migration(migrations.Migration):

    dependencies = [
        ('grantomy', '0005_alter_zeus_edad'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZeusDni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('front', models.ImageField(max_length=255, null=True, upload_to=pretix.base.models.items.itempicture_upload_to)),
                ('backend', models.ImageField(max_length=255, null=True, upload_to=pretix.base.models.items.itempicture_upload_to)),
            ],
        ),
    ]