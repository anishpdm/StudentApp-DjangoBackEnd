import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from students.serializers import StudentAppSerializer
from students.models import StudentModel
from django.db.models import Q


@csrf_exempt
def UpdateStudentDetails(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        getAdmno=recieved_data["admno"]
        getName=recieved_data["name"]
        getRoll=recieved_data["rollno"]
        getClg=recieved_data["college"]
        data=StudentModel.objects.filter(Q(admno__exact=getAdmno)).update(name=getName,rollno=getRoll,college=getClg)
        print(data)
        if data==1:
            return HttpResponse(json.dumps({"status":"Updated Successfully"}))
        else:
            return HttpResponse(json.dumps({"status":"Invalid Admno"}))  


@csrf_exempt
def DeleteStudentDetails(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        getAdmno=recieved_data["admno"]
        data=list(StudentModel.objects.filter(Q(admno__exact=getAdmno)).delete())
        print(data)
        if data[0]!=0:
            return HttpResponse(json.dumps({"status":"Deleted Successfully"}))
        else:
            return HttpResponse(json.dumps({"status":"Invalid Admno"}))    
        
    

@csrf_exempt
def viewAll(request):
    if request.method=="POST":
        studentList= StudentModel.objects.all()
        newStudentlist=StudentAppSerializer(studentList,many=True)
        return HttpResponse(json.dumps(newStudentlist.data))

@csrf_exempt
def SearchStudent(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        getAdmno=recieved_data["admno"]
        data=list(StudentModel.objects.filter(Q(admno__icontains=getAdmno)).values())
        return HttpResponse(json.dumps(data))
    
@csrf_exempt
def SearchStud(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        getAdmno=recieved_data["admno"]
        getRoll=recieved_data["rollno"]

        data=list(StudentModel.objects.filter( Q(admno__icontains=getAdmno) & Q(rollno__icontains=getRoll) ).values())
        return HttpResponse(json.dumps(data))

@csrf_exempt
def SearchStudById(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        getAdmno=recieved_data["id"]

        data=list(StudentModel.objects.filter( Q(id__icontains=getAdmno) ).values())
        return HttpResponse(json.dumps(data))

@csrf_exempt
def addStudent(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        print(json.dumps(recieved_data))
        student_serializer=StudentAppSerializer(data=recieved_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return HttpResponse(json.dumps({"status":"Success"}))
        else:
            return HttpResponse(json.dumps({"status":"Failed"}))

