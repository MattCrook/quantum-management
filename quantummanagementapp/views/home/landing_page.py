from django.shortcuts import render

def landing_page(request):
    if request.method == 'GET':
        template = 'landing_page.html'
        context = {}

        return render(request, template, context)


def home(request):
    if request.method == 'GET':
        template = 'home/home.html'
        context = {}

        return render(request, template, context)
