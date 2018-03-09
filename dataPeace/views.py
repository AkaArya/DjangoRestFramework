from __future__ import unicode_literals
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from .serializers import StudentSerializer2
from rest_framework import generics
from django.db.models import Q
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class StudentDetail(APIView):
    """
    Retrieve, update or delete a student instance against the 'id' parameter passed in URL
    GET,PUT,DELETE request
    """
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        student = self.get_object(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        """
        Uses a serializer which serializes through only 3 fields so that only those 3 fields can be updated.
        """
        student = self.get_object(id)
        serializer = StudentSerializer2(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentList(generics.ListCreateAPIView):
    """
        List or Create student instance.
        GET,POST request
        Restricts a student instance against the 'Page', 'limit', 'sort' parameters passed in Get request
        default limit is 5
     """
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    serializer_class = StudentSerializer


    def get_queryset(self):
        """
        Optionally restricts the student information,
        by filtering against a `name` query parameter in the URL.
        """
        queryset = Student.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(Q(first_name=name)|Q(last_name=name))
        return queryset