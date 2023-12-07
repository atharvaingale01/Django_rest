from .models import Drink
from .serializers import DrinkSerializers
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def drinklist(request,format = None):
    #get all the drinks
    #serializers them
    #return Json
    if request.method == 'GET':
        drinks = Drink.objects.all() #get all the drinks
        serializer = DrinkSerializers(drinks,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DrinkSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])

def drink_details(request,id,format = None):
    try:
        drink = Drink.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializers(drink)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = DrinkSerializers(drink,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        drink.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    