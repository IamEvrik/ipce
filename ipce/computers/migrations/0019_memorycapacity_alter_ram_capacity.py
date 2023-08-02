# Generated by Django 4.2.3 on 2023-08-02 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("computers", "0018_ramtype_alter_manufacturer_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MemoryCapacity",
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
                    "capacity",
                    models.CharField(
                        max_length=10, unique=True, verbose_name="capacity"
                    ),
                ),
            ],
            options={
                "verbose_name": "memory capacities",
            },
        ),
        migrations.AlterField(
            model_name="ram",
            name="capacity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="computers.memorycapacity",
                verbose_name="memory capacity",
            ),
        ),
    ]