from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import UserProfile, Space, Reservation
from .serializers import UserProfileSerializer, UserSerializer, CreateUserSerializer, SpaceSerializer,ReservationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
import mercadopago
import os


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateUserSerializer
        return UserSerializer

class SpaceViewSet(viewsets.ModelViewSet):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    
    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         return [permissions.AllowAny()]
    #     else:
    #         return [permissions.IsAuthenticated()]

    # def perform_create(self, serializer):
    #         serializer.save(owner=self.request.user)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset= Reservation.objects.all()
    serializer_class= ReservationSerializer

class PaymentView(APIView):
    
    def post(self, request):
        sdk = mercadopago.SDK("TEST-2092818577509647-022720-0a24cf2677acb29255e8f2c716fe1814-51067083")

        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {
            'x-idempotency-key': '123'
        }

        payment_data = {
            "transaction_amount": 100,
            "token": 'ff8080814c11e237014c1ff593b57b4d',
            "installments": 1,
            "payer": {
                "type": "customer",
                "id": "123456789-jxOV430go9fx2e"
            }
        }

        payment_response = sdk.payment().create(payment_data, request_options)
        payment = payment_response["response"]
