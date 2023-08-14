"""Загрузка информации из csv."""

import csv
import pathlib

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from software import models as softmodels


class Command(BaseCommand):
    """Выполнение загрузки."""

    DATA_DIR: pathlib.Path = settings.STATIC_ROOT / 'data'

    FILES_CLASSES_MAPPING = {
        'office_version.csv': softmodels.OfficeVersion,
        'office_key.csv': softmodels.OfficeKey,
        'os_version.csv': softmodels.OSVersion,
        'os_key.csv': softmodels.OSKey,
    }

    def handle(self, *args, **options):
        """Процедура загрузки."""
        with transaction.atomic():
            for filename, classname in Command.FILES_CLASSES_MAPPING.items():
                fullname = Command.DATA_DIR / filename
                if not fullname.exists():
                    raise CommandError(f'File {filename} does not exists.')

                with open(fullname, mode='r', encoding='utf8') as csv_file:
                    csv_dict = csv.DictReader(csv_file)
                    for element in csv_dict:
                        classname.objects.get_or_create(**element)
                self.stdout.write(f'File {filename} processed.\n')
