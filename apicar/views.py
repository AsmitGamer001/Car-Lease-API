from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Car,Lease
from django.http import JsonResponse
# Create your views here.
#test