from django.http import HttpResponse # type: ignore

def index(request):
    return HttpResponse("<h1> IA Avanzada</h1>")