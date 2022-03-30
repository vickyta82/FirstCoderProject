from django.contrib import admin
from django.urls import path
from DataBase1.views import professor, student, subject, paper, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('professor/', professor),
    path('student/', student),
    path('paper/', paper),
    path('subject/', subject)
]
