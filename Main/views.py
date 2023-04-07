from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def main(request):
    # response = render(request, 'Main/index.html')
    # return HttpResponse(response)
    try:
        response = render(request, 'Main/index.html')
        return HttpResponse(response)
    except:
        return HttpResponseNotFound('<h1>error main page</h1>')