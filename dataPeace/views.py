from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentList(APIView):

    def get(self, request,format=None):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        student = self.get_object(id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



