# Generated by Django 3.2.18 on 2023-03-28 18:11

from django.db import migrations, models
import grantomy.models


class Migration(migrations.Migration):

    dependencies = [
        ('grantomy', '0006_zeusdni'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZeusDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('document', models.BinaryField()),
            ],
        ),
        migrations.AlterField(
            model_name='zeusdni',
            name='backend',
            field=models.ImageField(max_length=255, null=True, upload_to=grantomy.models.itempicture_upload_to),
        ),
        migrations.AlterField(
            model_name='zeusdni',
            name='front',
            field=models.ImageField(max_length=255, null=True, upload_to=grantomy.models.itempicture_upload_to),
        ),
    ]