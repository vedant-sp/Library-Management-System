from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer,BookSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer



@api_view(['GET'])
def index(request):
    return Response({'Hello': 'World'})


@api_view(['GET'])
def bookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many = True)
    return Response(serializer.data)
    # return Response('data')

@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({'success':False})
    return Response({"success":True,'data': 'Book Sucessfully Added'})

@api_view(['POST'])
def update_book(request, pk):
    book = Book.objects.get(book_id=pk)
    serializer = BookSerializer(instance = book, data = request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({'success':False})
    return Response({'success':True,'data':serializer.data})

@api_view(['GET'])
def delete_book(request, pk):
    book = Book.objects.get(book_id=pk)
    book.delete()
    return Response({'data': "Book sucessfully deleted", 'success':True})

