# Generated by Django 4.2.3 on 2023-07-31 08:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("computers", "0007_alter_computer_os_bit_depth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="computer",
            name="ip_address",
            field=models.GenericIPAddressField(
                blank=True,
                null=True,
                protocol="IPv4",
                unique=True,
                verbose_name="IP address",
            ),
        ),
    ]