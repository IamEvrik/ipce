# Generated by Django 4.2.3 on 2023-07-31 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("computers", "0009_monitor_monitor_unique_monitor_name_serial_no"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserName",
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
                    "name",
                    models.CharField(
                        max_length=30, unique=True, verbose_name="username"
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="password"
                    ),
                ),
            ],
            options={
                "verbose_name": "username",
                "verbose_name_plural": "usernames",
            },
        ),
        migrations.AddField(
            model_name="computer",
            name="username",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="computers.username",
                verbose_name="username",
            ),
        ),
    ]