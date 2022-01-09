import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from .crawler import *
from rates.models import Rate


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_csv()

        try:
            with open(filepath, 'r', encoding='utf-8') as csvfile:
                csvreader = csv.DictReader(csvfile, delimiter=',')

                for row in csvreader:
                    try:
                        rate = Rate(crypto_name=row['Name'],
                                    usd_rate=row['USD rate'],
                                    pln_rate=row['PLN rate'],
                                    date=row['Data + Time'])

                        rate.save()
                    except Exception as e:
                        continue
        except:
            print("No such File")
