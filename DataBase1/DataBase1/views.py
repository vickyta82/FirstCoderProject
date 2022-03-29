from django.http import HttpResponse
from django.template import Template, Context

def professor(request):
    return HttpResponse("Faculty")
def student(request):    
    return HttpResponse("Student Info")

def start_up(request):
    file = open(r"C:\Users\vlapa\Desktop\Python\FirstCoderProject\DataBase1\DataBase1\templates\DBTemp1.html", 'r')    
    template1 = Template(file.read())

    file.close()

    context1 = Context()
    file = template1.render(context1)

    return HttpResponse(file)
    
