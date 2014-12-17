from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html", {})


def services(request):
    return render(request, "services.html", {})


def equipment(request):
    return render(request, "equipment.html", {})


def contact(request):
    return render(request, "contact.html", {})


def external(request):
    return render(request, "external.html", {})


def join(request):
    return render(request, "join.html", {})


def crew(request):
    return render(request, "crew.html", {})


def hots(request):
    return render(request, "hots.html", {})


def alumni(request):
    return render(request, "alumni.html", {})


def events(request):
    return render(request, "events.html", {})


def events70(request):
    return render(request, "events-1970.html", {})


def events80(request):
    return render(request, "events-1980.html", {})


def events90(request):
    return render(request, "events-1990.html", {})


def events00(request):
    return render(request, "events-2000.html", {})


def timelapse(request):
    return render(request, "timelapse.html", {})


def accolades(request):
    return render(request, "accolades.html", {})


def signup(request):
    d = request.POST
    andrew_id = d.get("andrew_id")
    name = d.get("name")
    print(andrew_id, name)
    return HttpResponse("hi")