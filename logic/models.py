"""
    App Models Definition
"""
from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as modelgis
from django.utils.timezone import now
from enum import Enum
import datetime


class EventState(Enum):
    VALIDATE = 'validar'
    VALID = 'validado'
    RESOLVED = 'resolvido'


class Event(models.Model):
    """
        Event entity definition

        Attributes:
            author (User): User that created the event
            description (str): Event description
            geo_location (PointField): Latitude and Longitude where the events was created
            creation_date (datetime): Timestamp when the event was generated
            updated_date (datetime): Timestamp when the event was updated the last time
            state (EventState): State in which the event is currently
    """
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='events')
    description = models.CharField(max_length=100)
    geo_location = modelgis.PointField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=9, default=EventState.VALIDATE,
                             choices=[(state.value, state.name) for state in EventState])

    class Meta:
        ordering = ['creation_date']


class Construction(Event):
    start_time = models.DateTimeField(default=now())


class SpecialEvent(Event):
    event_type = models.CharField(max_length=20, null=True)


class Incident(Event):
    pass


class Weather(Enum):
    """
        Weather conditions enum
    """
    RAIN = 'rainy'
    SUN = 'sunny'
    CLOUD = 'cloudy'


class WeatherCondition(Event):
    weather = models.CharField(max_length=10, null=True,
                               choices=[(weather.value, weather.name) for weather in Weather])


class RoadCondition(Event):
    pass
