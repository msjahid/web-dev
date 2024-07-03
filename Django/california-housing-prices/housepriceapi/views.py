from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
from .models import HousingData
from django.conf import settings  # Import the Django settings
import pickle5 as pickle
from housepriceapi.serializers.house_serializers import HousingDataSerializer
import warnings
from django.shortcuts import render

# Suppress the UserWarning
warnings.filterwarnings("ignore", category=UserWarning)

# Construct the absolute path to the model.pkl file
model_path = os.path.join(settings.BASE_DIR, 'ml_model', 'model.pkl')

# Load the trained machine learning model when the module is loaded
loaded_model = pickle.load(open(model_path, 'rb'))


def home(request):
    return render(request, 'housepriceapi/home.html')


@api_view(['POST'])
def predict_housing_price(request):
    if request.method == 'POST':
        # Deserialize input data using the serializer
        serializer = HousingDataSerializer(data=request.data)

        if serializer.is_valid():
            # Preprocess input data
            input_data = serializer.validated_data
            # Map the 'ocean_proximity' field using the same choices
            input_data['ocean_proximity'] = dict(HousingData.OCEAN_PROXIMITY_CHOICES).get(input_data['ocean_proximity'])

            try:
                # Make predictions using the loaded model
                predicted_price = loaded_model.predict([list(input_data.values())])  # Convert input_data to a list

                # Return predictions as a JSON response
                response_data = {
                    'The Median House Price is': int(predicted_price)
                }

                return Response(response_data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'error': 'Unsupported HTTP method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)