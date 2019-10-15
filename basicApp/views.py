from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'basicApp/home.html')


def index(request):
    d = {'text': 'hello world', 'numbers': 25}
    return render(request, 'basicApp/index.html', context=d)


def other(request):
    return render(request, 'basicApp/other.html')


def relative(request):
    return render(request, 'basicApp/relUrlTemp.html')
