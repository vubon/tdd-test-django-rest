import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse


from contacts.models import Contact
from contacts.serializers import ContactSerializers

client = Client()

