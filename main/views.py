# -- coding: utf-8 --
from django.shortcuts import render, get_object_or_404
from .models import Car, Sale
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Главная страница")

def cars_list_view(request):
    query = request.GET.get('q')
    if query:
        cars = Car.objects.filter(model__icontains=query)
    else:
        cars = Car.objects.all()
    return render(request, 'main/list.html', {'cars': cars})

def car_details_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'main/details.html', {'car': car})

def sales_by_car(request, car_id):
    sales = Sale.objects.filter(car_id=car_id)
    return render(request, 'main/sales.html', {'sales': sales})