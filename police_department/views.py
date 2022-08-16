import io
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
import csv
import time
import logging

from rest_framework import viewsets, mixins
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from .models import Calls
from .serializers import CallsSerializer


def upload_csv(request):
    template = 'index.html'

    if request.method == 'GET':
        return render(request, template)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    start_time = time.time()

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    reader = csv.reader(io_string, delimiter=';')

    for row in reader:
        row = str(row).replace('[', '').replace(']', '').replace("'", '').replace('"', '').split(',')
        row = [cell.strip() for cell in row]

        _, created = Calls.objects.update_or_create(
            crime_id=row[0],
            crime_type=row[1],
            report_date=datetime.strptime(row[2], '%Y-%m-%dT%H:%M:%S'),
            call_date=datetime.strptime(row[3], '%Y-%m-%dT%H:%M:%S'),
            offense_date=datetime.strptime(row[4], '%Y-%m-%dT%H:%M:%S'),
            call_time=row[5],
            call_date_time=datetime.strptime(row[6], '%Y-%m-%dT%H:%M:%S'),
            disposition=row[7],
            address=row[8],
            city=row[9],
            state=row[10],
            agency_id=row[11],
            address_type=None if row[12] == 'Common Location' else row[12],
            common_location=row[13] if row[13] else None
        )
    end_time = time.time()
    calls = Calls.objects.all().count()
    logging.basicConfig(filename='/Users/jetigenov/Desktop/logs.log', level=logging.INFO)
    logging.info(f'request time: {end_time - start_time}, '
                 f'calls: {calls}')

    return render(request, template)


@permission_classes((AllowAny,))
class CallsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CallsSerializer
    queryset = Calls.objects.all()

