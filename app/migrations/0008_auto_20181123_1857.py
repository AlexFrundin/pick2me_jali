# Generated by Django 2.1.2 on 2018-11-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181123_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentdrivers',
            name='button_one',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='contentdrivers',
            name='button_two',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='contentdrivers',
            name='header',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='about_one_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='about_one_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='about_p',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='about_three_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='about_three_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='about_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='about_two_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='about_two_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='conditions_descriptiom',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='conditions_one_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='conditions_one_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='conditions_three_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='conditions_three_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='conditions_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='conditions_two_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='conditions_two_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='download_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='download_p',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='download_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='step_one_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='step_one_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='step_three_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='step_three_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='step_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='step_two_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='step_two_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='taxi_app_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='taxi_app_title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='taxi_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='taxi_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
