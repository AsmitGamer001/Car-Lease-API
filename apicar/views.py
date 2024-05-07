from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Car,Lease
from django.http import JsonResponse
# Create your views here.
#test

def lease_car(request):
    if request.method == 'POST':
        data = request.POST
        driver_id=data.get('driverId')
        car_id=data.get('carId')
        try:
            car=Car.objects.get(id=car_id,status='available')
            car.status='leased'
            car.save()
            Lease.objects.create(driver_id=driver_id,car=car)
            return JsonResponse({'message':'Car Leased Succesfully','data':{'driverId':driver_id,'carId':car_id}},status=201)
        except:
            
