# Generated by Django 4.2.3 on 2023-08-22 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("computers", "0011_videocardmodel_videocard_computer_videocard"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hddmodel",
            name="capacity",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                to="computers.memorycapacity",
                verbose_name="capacity",
            ),
        ),
        migrations.CreateModel(
            name="ProcessorModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model", models.CharField(max_length=255, verbose_name="model")),
                (
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="computers.manufacturer",
                        verbose_name="manufacturer",
                    ),
                ),
            ],
            options={
                "verbose_name": "processor model",
                "verbose_name_plural": "processor models",
            },
        ),
        migrations.CreateModel(
            name="Processor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "serial_no",
                    models.CharField(max_length=255, verbose_name="serial number"),
                ),
                (
                    "model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="processors",
                        to="computers.processormodel",
                        verbose_name="model",
                    ),
                ),
            ],
            options={
                "verbose_name": "processor",
                "verbose_name_plural": "processors",
            },
        ),
        migrations.AlterField(
            model_name="computer",
            name="processor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="computers.processor",
                verbose_name="processor",
            ),
        ),
    ]