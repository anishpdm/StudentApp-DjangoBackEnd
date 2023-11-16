import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from students.serializers import StudentAppSerializer
from students.models import StudentModel
# Create your views here.

def viewAll(request):
    if request.method=="GET":
        vehicleapp_List=StudentModel.objects.all()
        VehicleAppDetailsSerializer=StudentAppSerializer(vehicleapp_List,many=True)
        return HttpResponse(json.dumps(VehicleAppDetailsSerializer.data))

        # return HttpResponse(json.dumps({"status":"hello"}))

@csrf_exempt
def addStudent(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        print(json.dumps(recieved_data))
        student_serializer=StudentAppSerializer(data=recieved_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return HttpResponse(json.dumps({"status":"Sucessfully Registered"}))
        else:
            return HttpResponse(json.dumps({"status":"Adding New vehicle Failed"}))

        return HttpResponse(json.dumps({"status":"student adding section"}))