from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Drivers, Logs
import datetime

class Index_view(View):
    def get(self, request):
        return render(request, 'core/index.html', context={})

class Request_view(View):
    def get(self, request):
        mode = request.GET['MODE']

        # запрос с параметрами MODE,ID и данные - вернет Ok либо ошибку
        if mode == 'add_log':
            try:
                driver = Drivers.objects.get(driver_id=request.GET['ID'])
                Logs.objects.create(
                    driver_id = driver,
                    created_at = datetime.datetime.now(),
                    speed = request.GET['SPEED'],
                    rpm = request.GET['RPM']
                )
                return HttpResponse('Ok')
            except Exception as e:
                return HttpResponse(e)

        # запрос с параметрами MODE и ID - вернет ФИО либо, что его нет
        if mode == 'connect':
            try:
                driver = Drivers.objects.get(driver_id=request.GET['ID'])
                return HttpResponse(str({
                    'surname': driver.surname,
                    'firstname': driver.firstname,
                    'patronymic': driver.patronymic,
                }))
            except:
                return HttpResponse('No_driver')
        