from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Drivers, Logs
import datetime

class Index_view(View):
    def get(self, request):
        logs = Logs.objects.all()
        return render(request, 'core/index.html', context={'logs' : logs})

class Api_insert_view(View):
    def get(self, request):
        try:
            driver = Drivers.objects.get(driver_id=request.GET['ID'])
            # Logs.objects.create(
            #     driver_id = driver,
            #     created_at = datetime.datetime.now(),
            #     speed = request.GET['SPEED'],
            #     rpm = request.GET['RPM']
            # )
            return HttpResponse('Ok')
        except Exception as e:
            return HttpResponse('Error')

class Api_connect_view(View):
    def get(self, request):
        try:
            driver = Drivers.objects.get(driver_id=request.GET['ID'])
            return HttpResponse(str(driver.surname + ' ' + driver.firstname + ' ' + driver.patronymic))
        except:
            return HttpResponse('Error')
        