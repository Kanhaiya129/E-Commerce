from django.urls import path
from . views import *

urlpatterns = [
    # path("login/", CustomerLoginView.as_view(), name="login"),
    path("customer_login/", CustomerRegistrationView.as_view(), name="customer_login"),
]