from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate
from logic.views import UserView
import json
# Test Post

# Create your tests here.
factory = APIRequestFactory()
# Get User
user = User.objects.get(id=1)
# Create View
view = UserView.as_view()

request = factory.get('/api/users')
force_authenticate(request, user=user)

# Point
point = {"latitude": 49.8782482189424, "longitude": 24.452545489}
# Event (Json)
event = {"description": "testDescription", "state": "validar", "geo_location": point}

request = factory.post('/api/events/', event, format='json')
assert event == json.loads(request.body)

# Construction Event (Json)
construction = {"description": "testDescription", "state": "validar", "geo_location": point, "start_time": "2020-01-28 19:27:07.374912"}

request = factory.post('/api/events/construction/', construction, format='json')
assert construction == json.loads(request.body)

# Special Event (Json)
special_event = {"description": "testDescription", "state": "validar", "geo_location": point, "event_type": "sport"}

request = factory.post('/api/events/special-event/', special_event, format='json')
assert special_event == json.loads(request.body)

# Incident Event (Json)
incident = {"description": "testDescription", "state": "validar", "geo_location": point}

request = factory.post('/api/events/incident/', incident, format='json')
assert incident == json.loads(request.body)

# Weather Condition Json
weather = {"description": "testDescription", "state": "validar", "geo_location": point, "weather": "rainy"}

request = factory.post('/api/events/weather-condition/', weather, format='json')
assert weather == json.loads(request.body)

# Road Condition Json
road_condition = {"description": "testDescription", "state": "validar", "geo_location": point}

request = factory.post('/api/events/road-condition/', road_condition, format='json')
assert road_condition == json.loads(request.body)
