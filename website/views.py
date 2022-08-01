from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    skills = [
        {"name": "Flutter", "icon": "icons/kevalvavaliya-flutter.svg"},
        {"name": "Android", "icon": "icons/kevalvavaliya-android.svg"},
        {"name": "HTML", "icon": "icons/kevalvavaliya-html.svg"},
        {"name": "CSS", "icon": "icons/kevalvavaliya-css.svg"},
        {"name": "JavaScript", "icon": "icons/kevalvavaliya-js.svg"},
        {"name": "Python", "icon": "icons/kevalvavaliya-python.svg"},
        {"name": "Django", "icon": "icons/kevalvavaliya-django.svg"},
        {"name": "Java", "icon": "icons/kevalvavaliya-java.svg"},
        {"name": "PHP", "icon": "icons/kevalvavaliya-php.svg"},
        {"name": "Firebase", "icon": "icons/kevalvavaliya-firebase.svg"},
        {"name": "MySQL", "icon": "icons/kevalvavaliya-mysql.svg"},
        {"name": "JQuery", "icon": "icons/kevalvavaliya-jquery.svg"},
        {"name": "Google Cloud", "icon": "icons/kevalvavaliya-googlecloud.svg"},
        {"name": "Dart", "icon": "icons/kevalvavaliya-dart.svg"},
        {"name":"Wordpress", "icon":"icons/kevalvavaliya-wordpress.svg"}
    ]
    data={
        "skills":skills
    }

    return render(request, "index.html",data)
