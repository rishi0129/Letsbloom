from rest_framework import generics, status
from .models import Books
from .serializer import BookSerializer
from django.db import IntegrityError
from rest_framework.response import Response

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            error_message = "This book already exists."
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        
        
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer