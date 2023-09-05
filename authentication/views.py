
from authentication.serializer import RegistrationSerializer
from django.utils import timezone

from django.db import transaction
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from authentication.models import (
    UserActivationOTP,
    ForgotPasswordSentOtp,
    ForgetPasswordToken,
)
from rest_framework.authtoken.models import Token
from authentication.serializer import user_response, send_activation_email_otp

class CustomerRegistrationView(APIView):
    """
    API View for Creating the user.
    """

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Generate OTP and save to the database
            otp = get_random_string(length=6, allowed_chars="0123456789")
            ActivationOTP.objects.create(user=user, otp=otp)

            # Send email with OTP to the user
            emailsender.send_activation_otp_email(user, otp)
            return Response(
                {
                    "status": True,
                    "message": "Registration successful",
                    "data": {"user_id": user.id},
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {
                    "status": False,
                    "message": "Registration failed",
                    "data": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )