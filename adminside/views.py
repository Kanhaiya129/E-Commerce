from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from adminside.serializer import CategoriesSerializer,ItemsSerializer
from adminside.models import Categories, Items
from services.pagination import CustomPagination

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginView(APIView):
    # Class-based view for user login
    def post(self, request, format=None):
        email = request.data.get("email")
        password = request.data.get("password")

        if email and password:
            try:
                # Fetch user with given email and is_superuser
                user_obj = User.objects.get(email=email, is_superuser=True)
            except User.DoesNotExist:
                user_obj = None

            if user_obj:
                username = user_obj.username
                user = authenticate(username=username, password=password)

                if user:
                    # Delete any previous stored token
                    Token.objects.filter(user=user_obj).delete()

                    # Generate a new Token
                    token, created = Token.objects.get_or_create(user=user_obj)

                    return Response(
                        {
                            "status": True,
                            "message": "Authentication Successful",
                            "data": {"token": token.key},
                        },
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {
                            "status": False,
                            "message": "Invalid Credentials",
                            "data": None,
                        },
                        status=status.HTTP_401_UNAUTHORIZED,
                    )
            else:
                return Response(
                    {"status": False, "message": "User not found", "data": None},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {
                    "status": False,
                    "message": "Email and password are required",
                    "data": None,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class CategoriesView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategoriesSerializer
    pagination_class = CustomPagination

    def get(self, request):
        category = Categories.objects.all()
        page = self.paginate_queryset(category)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data
        else:
            serializer = self.serializer_class(category, many=True)
            data = serializer.data
        return Response(
            {
                "status": True,
                "message": "Categories Fetched Successfully",
                "data": data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": True,
                "message": "Category Added Successfully",
                "data": None,
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        data = {
            "status": False,
            "message": serializer.errors(),
            "data": None,
        }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Categories.objects.get(pk=pk)
        except Categories.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        if category:
            serializer = CategoriesSerializer(category)
            return Response(serializer.data)
        return Response(
            {"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND
        )

    def put(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        if category:
            serializer = CategoriesSerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND
        )

    def delete(self, request, pk, *args, **kwargs):
        category = self.get_object(pk)
        if category:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND
        )


class ItemsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemsSerializer
    pagination_class = CustomPagination

    def get(self, request):
        items = Items.objects.all()
        page = self.paginate_queryset(items)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data
        else:
            serializer = self.serializer_class(items, many=True)
            data = serializer.data
        serializer = self.serializer_class(items, many=True)
        return Response(
            {
                "status": True,
                "message": "Items Fetched Successfully",
                "data": data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": True,
                "message": "Item Added Successfully",
                "data": None,
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        data = {
            "status": False,
            "message": serializer.errors,
            "data": None,
        }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Items.objects.get(pk=pk)
        except Items.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        item = self.get_object(pk)
        if item:
            serializer = ItemsSerializer(item)
            return Response(serializer.data)
        return Response(
            {"message": "Item not found"}, status=status.HTTP_404_NOT_FOUND
        )

    def put(self, request, pk, *args, **kwargs):
        item = self.get_object(pk)
        if item:
            serializer = ItemsSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"message": "Item not found"}, status=status.HTTP_404_NOT_FOUND
        )

    def delete(self, request, pk, *args, **kwargs):
        item = self.get_object(pk)
        if item:
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"message": "Item not found"}, status=status.HTTP_404_NOT_FOUND
        )