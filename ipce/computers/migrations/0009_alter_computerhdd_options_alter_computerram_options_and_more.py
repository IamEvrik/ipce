# Generated by Django 4.2.3 on 2023-08-14 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("computers", "0008_remove_monitor_manufacturer_remove_monitor_name_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="computerhdd",
            options={
                "verbose_name": "computer hdd",
                "verbose_name_plural": "computers hdd",
            },
        ),
        migrations.AlterModelOptions(
            name="computerram",
            options={
                "verbose_name": "computer RAM",
                "verbose_name_plural": "computers RAM",
            },
        ),
        migrations.CreateModel(
            name="MotherboardModel",
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
                "verbose_name": "motherboard model",
                "verbose_name_plural": "motherboard models",
                "ordering": ("manufacturer", "model"),
            },
        ),
        migrations.CreateModel(
            name="Motherboard",
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
                        to="computers.motherboardmodel",
                        verbose_name="model",
                    ),
                ),
            ],
            options={
                "verbose_name": "motherboard",
                "verbose_name_plural": "motherboards",
            },
        ),
        migrations.AddField(
            model_name="computer",
            name="motherboard",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="computers.motherboard",
                verbose_name="motherboard",
            ),
        ),
    ]
