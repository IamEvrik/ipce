# Generated by Django 4.2.3 on 2023-08-02 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("computers", "0016_manufacturer"),
    ]

    operations = [
        migrations.AddField(
            model_name="monitor",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="monitor",
                to="computers.manufacturer",
                verbose_name="manufacturer",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="monitor",
            name="name",
            field=models.CharField(max_length=255, verbose_name="model"),
        ),
    ]