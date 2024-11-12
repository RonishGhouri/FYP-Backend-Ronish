# authapp/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.permissions import IsArtist, IsManager, IsConsumer

User = get_user_model()

# Helper function to generate JWT tokens for a user
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Register view
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')
    role = request.data.get('role')

    if password != confirm_password:
        return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

    # Create the new user
    user = User.objects.create_user(username=username, email=email, password=password, role=role)
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Check if the user exists
    if not User.objects.filter(username=username).exists():
        return Response({'error': 'User is not registered'}, status=status.HTTP_400_BAD_REQUEST)

    # Authenticate the user
    user = authenticate(username=username, password=password)
    if user is not None:
        tokens = get_tokens_for_user(user)  # Generate JWT tokens
        return Response({
            'access': tokens['access'],
            'refresh': tokens['refresh'],
            'role': user.role
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)
    
# Artist-only view
@api_view(['GET'])
@permission_classes([IsArtist])
def artist_only_view(request):
    return Response({'message': 'Welcome, Artist!'})


# Manager-only view
@api_view(['GET'])
@permission_classes([IsManager])
def manager_only_view(request):
    return Response({'message': 'Welcome, Manager!'})



# Consumer-only view
@api_view(['GET'])
@permission_classes([IsConsumer])
def consumer_only_view(request):
    return Response({'message': 'Welcome, Consumer!'})
