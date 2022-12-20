from django.shortcuts import render,HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
# Create your views here.
from django.db.models import Q
def index(request):
    return render(request, 'index.html')

def allemp(request):
    emps = Employee.objects.all()
    context  =   {
        'emps' : emps
        }
   
    return render(request,'allemp.html', context)
def addemp(request):
    if request.method =='POST':
       name= request.POST['name']
       salary = int(request.POST['salary'])
       dept = int(request.POST['dept'])
       role = int(request.POST['role'])
       new_emp=Employee(name= name,salary = salary,dept_id= dept,role_id=role,hire_date=datetime.now())
       new_emp.save()
       return HttpResponse('employee saved successfully')
    
    elif request.method=='GET':
            
        return render(request,'addemp.html')
    else:
        return HttpResponse('an exception occured!')
def removeemp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee REMOVED SUCCESSFULLY")
        except:
            return HttpResponse("please eneter a valid name")    
    emps = Employee.objects.all()
    context={
        'emps': emps
    }
    return render(request,'removeemp.html',context)
def filteremp(request):
    if request.method =='POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role= request.POST['role']
        emps =Employee.objects.all()
        if name:
            emps = emps.filter(Q(name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)

        context ={
            'emps':emps
        }
        return render(request,'allemp.html',context)
    elif request.method=='GET':
        return render(request,'filteremp.html')
    else:
        return HttpResponse("nhi h ")
def rish(request):
    return render(request,'rish.html')

