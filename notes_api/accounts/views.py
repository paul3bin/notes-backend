from rest_framework import generics
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    # to create new user in the system
    serializer_class = UserSerializer
