from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from PhoneReview.models import Review, Brand, PhoneModel
import logging
logging.basicConfig(level=logging.DEBUG)

def main(request):
    try:
        phoneModels = Brand.objects.all()
        response = render(request, 'PhoneReview/index.html', {'models': phoneModels})
        return HttpResponse(response)
    except:
        return HttpResponseNotFound('<h1>Phone models page crashed</h1>')
    
def specificModel(request, model):    
    try:
        brand = Brand.objects.get(name=model)
        logging.debug(f"model: {model}")
        logging.debug(f"brand: {brand}")
        brand_phones = PhoneModel.objects.filter(brand=brand)
        response = render(request, 'PhoneReview/specificModels.html', {'models': brand_phones, 'brand': model})
        return HttpResponse(response)
    except:
        return HttpResponseNotFound('<h1>Specific models page crashed</h1>')
    
def reviews(request, model, slug):    
    try:
        reviews = Review.objects.filter(models__slug=slug)
        response = render(request, 'Main/index.html', {'reviews': reviews})
        return HttpResponse(response)
    except:
        return HttpResponseNotFound('<h1>Review page crashed</h1>')