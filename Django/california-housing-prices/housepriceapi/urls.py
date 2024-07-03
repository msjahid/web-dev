from django.urls import path, include
from . import views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    # Define the API endpoint for predicting housing prices
    # path('form/', views.HousingDataForm, name='HousingDataForm'),
    path('', views.home, name='home'),
    path('predict/', views.predict_housing_price, name='predict_housing_price'),
]