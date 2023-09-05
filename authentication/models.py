from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import binascii
import os


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=50, null=True, blank=True)
    fcm_token = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.user.email


class ActivationOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Activation OTP {self.otp} for {self.user.email}"

    def save(self, *args, **kwargs):
        if not self.id:
            # Set the expiration time to 5 minutes from the current time
            self.expires_at = timezone.now() + timezone.timedelta(minutes=5)
        super().save(*args, **kwargs)


class ForgetPasswordOtp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"OTP {self.otp} for {self.user.email}"

    def save(self, *args, **kwargs):
        if not self.id:
            # Set the expiration time to 5 minutes from the current time
            self.expires_at = timezone.now() + timezone.timedelta(minutes=5)
        super().save(*args, **kwargs)


class ForgetPasswordToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_token()
        return super().save(*args, **kwargs)

    def generate_token(self):
        return binascii.hexlify(os.urandom(20)).decode()

    class Meta:
        verbose_name = "Forget Password Token"
        verbose_name_plural = "Forget Password Tokens"
