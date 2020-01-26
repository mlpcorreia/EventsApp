"""
    Entities Model Serializers
"""
from django.contrib.auth.models import User, Group
from logic.models import Event, EventState, Construction, SpecialEvent, Incident, WeatherCondition, Weather, RoadCondition
from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups', 'events']


class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=100)
    state = serializers.ChoiceField(choices=[(state.value, state.name) for state in EventState],
                                    default=EventState.VALIDATE.value)
    author = User()
    geo_location = PointField()

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance


class ConstructionSerializer(EventSerializer):
    start_time = serializers.DateTimeField()

    def create(self, validated_data):
        return Construction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.state = validated_data.get('state', instance.state)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.save()
        return instance


class SpecialEventSerializer(EventSerializer):
    event_type = serializers.CharField(max_length=20, default=None)

    def create(self, validated_data):
        return SpecialEvent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.state = validated_data.get('state', instance.state)
        instance.event_type = validated_data.get('event_type', instance.event_type)
        instance.save()
        return instance


class IncidentSerializer(EventSerializer):
    def create(self, validated_data):
        return Incident.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance


class WeatherConditionSerializer(EventSerializer):
    weather = serializers.ChoiceField(choices=[(weather.value, weather.name) for weather in Weather], default=None)

    def create(self, validated_data):
        return WeatherCondition.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance


class RoadConditionSerializer(EventSerializer):
    def create(self, validated_data):
        return RoadCondition.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance
