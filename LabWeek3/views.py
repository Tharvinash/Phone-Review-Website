from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from PhoneReview.models import PhoneModel

# Create your views here.
def login(request):
    try:
        response = render(request, 'LabWeek3/login.html')
        return HttpResponse(response)
    except:
        return HttpResponseNotFound('<h1>Login page crashed</h1>')
    
def register(request):
    try:
        response = render(request, 'LabWeek3/register.html')
        return HttpResponse(response)
    except:
        return HttpResponseNotFound('<h1>Register page crashed</h1>')
    
def addReview(request):
    phoneModels = PhoneModel.objects.all()
    try:
        response = render(request, 'LabWeek3/add-review.html', {'phoneModels': phoneModels})
        return HttpResponse(response)
    except:
        return HttpResponseNotFound('<h1>Add review page crashed</h1>')