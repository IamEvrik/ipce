# Generated by Django 4.2.3 on 2023-08-14 12:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("software", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="officekey",
            options={
                "ordering": ("office_version", "key_text"),
                "verbose_name": "office key",
                "verbose_name_plural": "office keys",
            },
        ),
        migrations.AlterModelOptions(
            name="oskey",
            options={
                "ordering": ("os_version", "key_text"),
                "verbose_name": "OS key",
                "verbose_name_plural": "OS keys",
            },
        ),
    ]
