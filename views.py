from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework import status, serializers
from rest_framework.generics import get_object_or_404

from .models import Hope
from .serializer import HopeSerializer
# Create your views here.
from rest_framework.response import Response




@api_view(['GET','POST'])
def hope_list(request):
    if request.method == 'GET':
        #get all the hopes
        #serialize them
        #return json
        hopes = Hope.objects.all()
        serializer=HopeSerializer(hopes, many=True)
        return JsonResponse({'hopes':serializer.data}, safe=False)
    if request.method == 'POST':
        serializer=HopeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def hope_detail(request, id):
    try:
        hope = Hope.objects.get(pk=id)
    except Hope.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HopeSerializer(hope)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HopeSerializer(hope, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hope.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




