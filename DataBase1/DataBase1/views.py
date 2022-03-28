from django.http import HttpResponse
from django.template import Template, Context

def greeting(request):
    return HttpResponse("Welcome from my first Django based website")
def thankyou(request):    
    return HttpResponse("<h1> Thanks </h1> <p> Sebas and Eze for helping me</P>")

def start_up(request):
    file = open(r"C:\Users\vlapa\Desktop\Python\FirstCoderProject\DataBase1\DataBase1\templates\DBTemp1.html", 'r')    
    template1 = Template(file.read())

    file.close()

    context1 = Context()
    file = template1.render(context1)

    return HttpResponse(file)
    
