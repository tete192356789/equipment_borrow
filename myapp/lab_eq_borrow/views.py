from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect,JsonResponse
from django.template import loader
from .models import *
from django.urls import reverse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *

# Create your views here.
def index(request):
    objs = Item.objects.all().values()
    json_data = []
    for obj in objs:
        json_data.append(obj)

    return JsonResponse(json_data, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def all_faculties(request):
    allfaculties = Facultie.objects.all()
    serializer = FacultiesSerializer(allfaculties,many = True)
    return Response(serializer.data,status = status.HTTP_200_OK)

@api_view(['GET'])
def all_items(request):
    allitems = Item.objects.all()
    serializer = ItemsSerializer(allitems,many = True)
    return Response(serializer.data,status = status.HTTP_200_OK)