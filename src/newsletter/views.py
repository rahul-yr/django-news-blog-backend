from django.shortcuts import render
from .models import Newsletter,ContactForm
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import views, mixins, permissions, exceptions, status
from rest_framework.utils import json
from . import serializers

# Create your views here.

@api_view(['POST'])
def subscribe_to_newsletter(request):
    print(request.data)
    if Newsletter.objects.filter(email = request.data['email']).exists():
        instance =  Newsletter.objects.filter(email = request.data['email'])[0]
        serializer = serializers.CreateNewsletterSerializer(instance,data = request.data)
    else:
        serializer = serializers.CreateNewsletterSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Subscribed Successfully'}, status=200)
    return Response({'message':'something went wrong!'})

@api_view(['POST'])
def submit_contact_form(request):
    serializer = serializers.CreateContactFormSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Thank you for reaching out. We will get back to you shortly.'}, status=200)
    return Response({'message':'something went wrong!'})