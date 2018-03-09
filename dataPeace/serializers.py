from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer which serializes through all fields
    """
    class Meta:
        model= Student
        fields = '__all__'


class StudentSerializer2(serializers.ModelSerializer):
    """
    Serializer which serializes through 3 fields for PUT request
    """
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'age')