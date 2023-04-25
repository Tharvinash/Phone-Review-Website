from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from PhoneReview.models import PhoneModel
from .forms import ReviewForm
from django.urls import reverse
from django.utils import timezone

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
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            current_datetime = timezone.now()
            form.instance.date_published = current_datetime

            form.save()
            redirect_url = reverse('model-list')
            return HttpResponseRedirect(redirect_url)
    else:
        form = ReviewForm()

    try:
        response = render(request, 'LabWeek3/add-review.html', {
            'form': form,
            })
        return HttpResponse(response)
    except:
        return HttpResponseNotFound('<h1>Add review page crashed</h1>')
