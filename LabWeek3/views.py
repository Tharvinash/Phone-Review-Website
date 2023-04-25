from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from PhoneReview.models import PhoneModel
from .forms import ReviewForm

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
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = ReviewForm()

    try:
        response = render(request, 'LabWeek3/add-review.html', {
            'form': form,
            'phoneModels': phoneModels
            })
        return HttpResponse(response)
    except:
        return HttpResponseNotFound('<h1>Add review page crashed</h1>')
