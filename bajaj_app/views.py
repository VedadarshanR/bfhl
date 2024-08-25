from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataInputSerializer

data_store = []
HARD_CODED_RESPONSE = {
    "is_success": True,
    "user_id": "vedadarshan_r_01062003",
    "email": "vedadarshanramu@gmai.com",
    "roll_number": "21BCE1059"
}


@api_view(['GET', 'POST'])
def handle_data(request):
    if request.method == 'GET':
        
        return Response({"operation_code": 1}, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = DataInputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data.get('data', [])
            
            numbers = [item for item in data if item.isdigit()]
            alphabets = [item for item in data if item.isalpha()]
            highest_lowercase_alphabet = [max(filter(str.islower, alphabets), default="")]

            response_data = {
                **HARD_CODED_RESPONSE,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": highest_lowercase_alphabet
            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
