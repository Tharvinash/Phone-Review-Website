from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from PhoneReview.models import Review

# Create your views here.
def main(request):
    # response = render(request, 'Main/index.html')
    # return HttpResponse(response)
    try:
        reviews = Review.objects.all()
        response = render(request, 'Main/index.html', {'reviews': reviews})
        return HttpResponse(response)
    except:
        return HttpResponseNotFound('<h1>Index page crashed</h1>')