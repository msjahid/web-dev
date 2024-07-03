from rest_framework import serializers
from housepriceapi.models import HousingData


# House Create Serializer
class HousingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingData
        fields = '__all__'
