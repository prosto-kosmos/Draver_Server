from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Drivers, Logs
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

class Index_view(View):
    def get(self, request):
        logs = Logs.objects.all()
        return render(request, 'core/index.html', context={'logs' : logs})

@csrf_exempt
def api_insert_view(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            driver = Drivers.objects.get(driver_id=payload['ID'])
            data = json.loads(payload['DATA'])
            for item in data:
                Logs.objects.create(
                    driver_id = driver,
                    created_at = item['DateTime'],
                    speed = item['Speed'][:-4],
                    rpm = item['Rpm'][:-3],
                    coolantTemp = item['CoolantTemp'][:-1],
                    massAirFlow = item['MassAirFlow'][:-3],
                    throttlePosition = item['ThrottlePosition']
                )
            return HttpResponse('Ok')
        except Exception as e:
            return HttpResponse('Error')

@csrf_exempt
def api_connect_view(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            driver = Drivers.objects.get(driver_id=payload['ID'])
            return HttpResponse(str(driver.surname + ' ' + driver.firstname + ' ' + driver.patronymic))
        except:
            return HttpResponse('Error')