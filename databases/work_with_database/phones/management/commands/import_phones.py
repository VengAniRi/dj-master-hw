import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', newline='') as csvfile:
            phone_reader = csv.DictReader(csvfile, delimiter=';')
            for row in phone_reader:
                del(row[None])
                Phone.objects.create(**row)
