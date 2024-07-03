from django.db import models


# Create your models here.
class HousingData(models.Model):
    OCEAN_PROXIMITY_CHOICES = (
        ('NEAR BAY', 0),
        ('<1H OCEAN', 1),
        ('INLAND', 2),
        ('NEAR OCEAN', 3),
        ('ISLAND', 4)
    )

    housing_median_age = models.IntegerField(default=0)
    total_rooms = models.IntegerField(default=0)
    total_bedrooms = models.FloatField(default=0.0)
    population = models.IntegerField(default=0)
    households = models.IntegerField(default=0)
    median_income = models.FloatField(default=0.0)
    ocean_proximity = models.CharField(max_length=50, choices=OCEAN_PROXIMITY_CHOICES)

    def __str__(self):
        return f'Housing Data ID: {self.ocean_proximity}'
