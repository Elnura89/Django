from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# .\myVirt\Scripts\
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# admin.py -from .models import *

# Create your views here.
def index(request):

    name='Elnura'
    lastname='Min'
    age='30'
    address='Osh'

    students_list=['Ali', 'Badi', '3', '4', '5']

    context={'name':name, 'lastname':lastname, 'age':age, 'address':address, 'students':students_list}
    

    return render(request, 'index.html', context)



# class Student():
#     def __init__(self, name, lastname, age):
#         self.name=name
#         self.lastname=lastname
#         self.age=age
    
# def about(request):
    # students_list=[]   
    # S1=Student('Tim', 'Kim', '18') 
    # S2=Student('Rim', 'Lom', '19')  
    # S3=Student('Tom', 'Dom', '20') 
    # S4=Student('Som', 'Bom', '21')
    # S5=Student('Cod', 'Tok', '22')
    # students_list.append(S1)
    # students_list.append(S2)
    # students_list.append(S3)
    # students_list.append(S4)
    # students_list.append(S5)
    # context={'students':students_list}

    # rows = Students.objects.all()
    # context = {
    #     'students':rows
    # }
    # return render(request, 'index1.html', context)    
    
class Appliances():
    def __init__(self, name, description):
        self.name=name
        self.description=description

def techFunc(request):
    rows = Tech.objects.all()
    context = {
        'tech_list':rows
    }
    return render(request, 'index2.html', context) 

def contacts(request):

    # name=''
    # username=''
    

    # context={'name':name, 'username':username}
    

    return render(request, 'contacts.html')

def contactPost(request):

    # принять запрос
    fullname=request.POST.get('fullname')
    mail=request.POST.get('mail')

    newRow=Contacts.objects.create(fullname=fullname, mail=mail)
    newRow.save()
    return index(request)