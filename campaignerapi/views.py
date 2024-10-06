from django.shortcuts import render
from rest_framework import (
    mixins,
    viewsets,
)

from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny

from campaignerapi.models import Messages
from campaignerapi.serializers import MessagesSerializer


class MessagesViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,):

    serializer_class = MessagesSerializer
    queryset = Messages.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Create a comment for an episode
        """
        self.event = "CREATE_MESSAGES"
        return super().create(request, *args, **kwargs)

    # def create(self, request):
    #     serializer = MessagesSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         # Access validated data
    #         # name = serializer.validated_data['name']
    #         # email = serializer.validated_data['email']
    #         # age = serializer.validated_data['age']
    #
    #         # Process the data (e.g., save to the database)
    #         # MyModel.objects.create(name=name, email=email, age=age)
    #         # Or return it as a success response
    #         return Response({"message": "Message created successfully", "data": serializer.validated_data},
    #                         status=status.HTTP_201_CREATED)
    #
    #     # If the data is invalid, return validation errors
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)