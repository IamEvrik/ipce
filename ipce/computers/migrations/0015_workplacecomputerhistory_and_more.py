# Generated by Django 4.2.3 on 2023-08-01 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("computers", "0014_remove_computer_user_remove_computer_username_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkplaceComputerHistory",
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
                ("install_date", models.DateField(verbose_name="install date")),
                (
                    "computer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workplace_history",
                        to="computers.computer",
                        verbose_name="computer",
                    ),
                ),
                (
                    "workplace",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="computer_history",
                        to="computers.workplace",
                        verbose_name="work place",
                    ),
                ),
            ],
            options={
                "verbose_name": "Workplace computers",
                "verbose_name_plural": "workplaces computers",
            },
        ),
        migrations.AddConstraint(
            model_name="workplacecomputerhistory",
            constraint=models.UniqueConstraint(
                fields=("workplace", "computer", "install_date"),
                name="unique_workplace_computer_history",
            ),
        ),
    ]
