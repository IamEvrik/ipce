# Generated by Django 4.2.4 on 2023-08-21 07:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "computers",
            "0009_alter_computerhdd_options_alter_computerram_options_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="rammodel",
            name="model",
            field=models.CharField(max_length=255, verbose_name="model"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="hddmodel",
            name="model",
            field=models.CharField(max_length=255, verbose_name="model"),
        ),
    ]
