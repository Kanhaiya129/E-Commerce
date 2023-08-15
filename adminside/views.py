from django.shortcuts import render
from rest_framework.views import APIView

class CategoriesView(APIView):

    def post(self, request):
       data = request.data
       pass