from django.test import TestCase
from rest_framework.test import APIRequestFactory

# Create your tests here.
factory = APIRequestFactory()

request = factory.post('/events/', {"description": "testDescription", "state": "validar", "geo_location": {"latitude": 49.8782482189424, "longitude": 24.452545489}})
print(request.body)

a = {"latitude": 49.8782482189424, "longitude": 24.452545489}
