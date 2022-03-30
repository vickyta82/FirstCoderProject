from django.http import HttpResponse
from django.template import Context, Template, loader


def professor(request):
    return HttpResponse("Faculty")

def student(request):    
    name = "Victoria"
    last_name = "Lapadula"
    id = 29698410
    
    dict_context = {"name": name, "last_name": last_name, "id": id}
    template = loader.get_template("student.html")
    file = template.render(dict_context)
    return HttpResponse(file)

def subject(request):
    return HttpResponse("Course")
def paper(request):
    return HttpResponse("Papers")


    
    
