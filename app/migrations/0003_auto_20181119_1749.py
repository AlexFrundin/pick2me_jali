# Generated by Django 2.1.2 on 2018-11-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181117_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentclients',
            name='download_app',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contentclients',
            name='download_app_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
