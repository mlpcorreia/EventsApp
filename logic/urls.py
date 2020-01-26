"""
    REST API paths
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from logic import views

urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('events/', views.EventView.as_view()),
    path('events/<int:pk>/', views.EventViewDetail.as_view()),
    path('events/construction/', views.ConstructionView.as_view()),
    path('events/construction/<int:pk>/', views.ConstructionViewDetail.as_view()),
    path('events/special-event/', views.SpecialEventView.as_view()),
    path('events/special-event/<int:pk>/', views.SpecialEventViewDetail.as_view()),
    path('events/incident/', views.IncidentView.as_view()),
    path('events/incident/<int:pk>/', views.IncidentViewDetail.as_view()),
    path('events/weather-condition/', views.WeatherConditionView.as_view()),
    path('events/weather-condition/<int:pk>/', views.WeatherConditionViewDetail.as_view()),
    path('events/road-condition/', views.RoadConditionView.as_view()),
    path('events/road-condition/<int:pk>/', views.RoadConditionViewDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
