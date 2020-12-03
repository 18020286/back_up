from django.shortcuts import render
from courses.models import Course
# Create your views here.


def home_view(request):
    record_list = Course.objects.all()
    return render(request, 'home.html', {
        'object_list': record_list,
        'nav': 'home'
    })


def about_view(request):
    return render(request, 'about.html', {
        'nav': 'about'
    })

