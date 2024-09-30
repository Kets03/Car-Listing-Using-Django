from django.shortcuts import render, get_object_or_404
from .models import car

def car_list(request):
    cars = car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def car_detail(request, id):
    Car = get_object_or_404(car, id=id)
    return render(request, 'car_detail.html', {'car': Car})
