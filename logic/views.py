"""
    REST API views for the different entities.
    @GET, @POST, @PUT, @DELETE
"""
from django.contrib.auth.models import User, Group
from django.http import Http404
from logic.models import Event, Construction, SpecialEvent, Incident, WeatherCondition, RoadCondition
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from logic.serializers import UserSerializer, EventSerializer, ConstructionSerializer, \
    SpecialEventSerializer, IncidentSerializer, WeatherConditionSerializer, RoadConditionSerializer


class UserView(APIView):
    def get(self, request, format=None):
        queryset = User.objects.all().order_by('-id')
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class UserViewDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventView(APIView):
    def get(self, request, format=None):
        queryset = Event.objects.all().order_by('-id')
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        user = request.user
        if serializer.is_valid() and isinstance(user, User):
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class EventViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ConstructionView(APIView):
    def get(self, request, format=None):
        queryset = Construction.objects.all().order_by('-id')
        serializer = ConstructionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ConstructionSerializer(data=request.data)
        user = request.user
        if serializer.is_valid() and isinstance(user, User):
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ConstructionViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Construction.objects.get(pk=pk)
        except Construction.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        construction = self.get_object(pk)
        serializer = ConstructionSerializer(construction)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        construction = self.get_object(pk)
        serializer = ConstructionSerializer(construction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        construction = self.get_object(pk)
        construction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SpecialEventView(APIView):
    def get(self, request, format=None):
        queryset = SpecialEvent.objects.all().order_by('-id')
        serializer = SpecialEventSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SpecialEventSerializer(data=request.data)
        user = request.user
        if serializer.is_valid() and isinstance(user, User):
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SpecialEventViewDetail(APIView):
    def get_object(self, pk):
        try:
            return SpecialEvent.objects.get(pk=pk)
        except SpecialEvent.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = SpecialEventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = SpecialEventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IncidentView(APIView):
    def get(self, request, format=None):
        queryset = Incident.objects.all().order_by('-id')
        serializer = IncidentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IncidentSerializer(data=request.data)
        user = request.user
        if serializer.is_valid() and isinstance(user, User):
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class IncidentViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Incident.objects.get(pk=pk)
        except Incident.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        incident = self.get_object(pk)
        serializer = IncidentSerializer(incident)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        incident = self.get_object(pk)
        serializer = IncidentSerializer(incident, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        incident = self.get_object(pk)
        incident.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WeatherConditionView(APIView):
    def get(self, request, format=None):
        queryset = WeatherCondition.objects.all().order_by('-id')
        serializer = WeatherConditionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WeatherConditionSerializer(data=request.data)
        user = request.user
        if serializer.is_valid() and isinstance(user, User):
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class WeatherConditionViewDetail(APIView):
    def get_object(self, pk):
        try:
            return WeatherCondition.objects.get(pk=pk)
        except WeatherCondition.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        weather = self.get_object(pk)
        serializer = WeatherConditionSerializer(weather)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        weather = self.get_object(pk)
        serializer = WeatherConditionSerializer(weather, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        weather = self.get_object(pk)
        weather.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoadConditionView(APIView):
    def get(self, request, format=None):
        queryset = RoadCondition.objects.all().order_by('-id')
        serializer = RoadConditionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoadConditionSerializer(data=request.data)
        user = request.user
        if serializer.is_valid() and isinstance(user, User):
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class RoadConditionViewDetail(APIView):
    def get_object(self, pk):
        try:
            return RoadCondition.objects.get(pk=pk)
        except RoadCondition.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        road = self.get_object(pk)
        serializer = RoadConditionSerializer(road)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        road = self.get_object(pk)
        serializer = RoadConditionSerializer(road, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, format=None):
        road = self.get_object(pk)
        road.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
