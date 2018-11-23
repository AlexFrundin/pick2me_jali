# Generated by Django 2.1.2 on 2018-11-19 22:35

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_contentclients_about_first_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentclients',
            name='about_first_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='about_five_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='about_four_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='about_second_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='about_six_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='about_third_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='clothes_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='dishes_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='download_app_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='food_box_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='food_delivery_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='main_descrription',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='mobile_app_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='pills_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='taxi_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentclients',
            name='track_order_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='about_one_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='about_three_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='about_two_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='download_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='register_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='step_one_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='step_three_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='step_two_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='taxi_description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='contentdrivers',
            name='title_descriptiom',
            field=tinymce.models.HTMLField(),
        ),
    ]