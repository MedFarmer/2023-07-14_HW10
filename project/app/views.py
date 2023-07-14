from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'index.html', context)

def adding_id(request):    
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'adding_id.html', context)

def add_student(request):
    if request.method == 'POST':
        students = request.POST
        if students['fname'] != '': # this is to be sure that no inputs are empty
            name = students['fname']
            add = Student()
            add.fname = name            
            add.save()
            return redirect('index')
        else:
            return render(request, 'add_student.html')    
    else:
        return render(request, 'add_student.html')

def delete(request):
    students = Student.objects.all()
    
    for student in students:
        if int(student.id) % 2 != 0:
            student.delete()
    return redirect('index')