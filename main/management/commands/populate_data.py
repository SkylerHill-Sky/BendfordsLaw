import csv
import math

from django.core.management.base import BaseCommand, CommandError
from main.models import DemographicData


class Command(BaseCommand):
    help = 'Populates the DB from our CSV census file'

    def handle(self, *args, **options):
        with open('acs2015_county_data.csv', 'r') as f:
            reader = csv.reader(f, delimiter=",")
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                try:
                    DemographicData.objects.create(
                        census_id=int(row[0]),
                        state=row[1],
                        county=row[2],
                        total_pop=int(row[3]),
                        total_men=int(row[4]),
                        total_women=int(row[5]),
                        hispanic=float(row[6]),
                        white=float(row[7]),
                        black=float(row[8]),
                        native=float(row[9]),
                        asian=float(row[10]),
                        pacific=float(row[11]),
                        citizen=int(row[12]),
                        income=int(float(row[13])),
                        income_err=int(float(row[14])),
                        income_per_cap=int(float(row[15])),
                        income_per_cap_err=int(float(row[16])),
                        poverty=float(row[17]),
                        child_poverty=float(row[18]),
                        professional=float(row[19]),
                        service=float(row[20]),
                        office=float(row[21]),
                        construction=float(row[22]),
                        production=float(row[23]),
                        drive=float(row[24]),
                        carpool=float(row[25]),
                        transit=float(row[26]),
                        walk=float(row[27]),
                        other_transportation=float(row[28]),
                        work_at_home=float(row[29]),
                        mean_commute=float(row[30]),
                        employed=int(row[31]),
                        private_work=float(row[32]),
                        public_work=float(row[33]),
                        self_employed=float(row[34]),
                        family_work=float(row[35]),
                        unemployment=float(row[36]),
                    )
                except Exception as e:
                    print(e)
        print('Data update complete!')
