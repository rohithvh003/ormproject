from django.shortcuts import render 
from myapp.models import Student 
# Create your views here. 
def StudentView(request): 
    s=Student.objects.all() 
    d={'stud':s} 
    return render(request,'C:/Users/Rohith/ormproject/templates/htmlpages/1.html',d) 
