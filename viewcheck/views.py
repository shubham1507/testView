from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello,Deepa Mathur, hope you can see view")