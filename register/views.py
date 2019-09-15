from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from register.models import fac
from . import models
from django.shortcuts import render,redirect



def registerfacVehicle(request):
    if request.method == 'POST':
        obj = fac()
        obj.name = request.POST["name"]
        obj.vehicle_no = request.POST["vehicle_no"]
        obj.vehicle_type = request.POST["type"]
        obj.des = request.POST["des"]
        obj.save()
        return redirect('/')
    return render(request,'register/register_base.html')

def veh(request):
    try:
        fac.objects.get(vehicle_no=request.POST["vehno"])
        return redirect('/register')
    except:
        return redirect('/groups')