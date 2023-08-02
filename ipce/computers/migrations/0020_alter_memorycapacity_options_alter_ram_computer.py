# Generated by Django 4.2.3 on 2023-08-02 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("computers", "0019_memorycapacity_alter_ram_capacity"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="memorycapacity",
            options={
                "ordering": ("capacity",),
                "verbose_name": "memory capacity",
                "verbose_name_plural": "memory capacities",
            },
        ),
        migrations.AlterField(
            model_name="ram",
            name="computer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="computers.computer",
                verbose_name="computer",
            ),
        ),
    ]
