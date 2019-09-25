from django.shortcuts import render
from django.http import HttpResponse
from . forms import UserForm

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")        # получение значения поля age
        print('Твой возраст - ',age,' лет')
        return HttpResponse("<h2>Hello, {0}! Тебе уже {1}.</h2>".format(name,age))
    else:
        userform = UserForm()
        return render(request, "firstapp/index.html", {"form": userform})
