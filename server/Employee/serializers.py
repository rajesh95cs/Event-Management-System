from rest_framework import serializers
from Employee.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = Employee
        fields = ("Empfirst_name", "Emplast_name", "Emp_des", "hired_date")
