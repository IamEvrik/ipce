# Generated by Django 4.2.3 on 2023-08-03 13:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("computers", "0002_hddtype_hdd"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="computer",
            name="has_ssd",
        ),
    ]
