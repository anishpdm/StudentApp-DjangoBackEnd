
from rest_framework import serializers
from students.models import StudentModel


class StudentAppSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields=(

           'name',
            'admno',
            'rollno',
            'college'
            
        )

