from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from PhoneReview.models import Brand, PhoneModel
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
        brand = Brand.objects.get(name=model)
        logging.debug(f"model: {model}")
        logging.debug(f"brand: {brand}")
        brand_phones = PhoneModel.objects.filter(brand=brand)
        response = render(request, 'PhoneReview/specificModels.html', {'models': brand_phones, 'brand': model})
        return HttpResponse(response)
    # try:
    # except:
    #     return HttpResponseNotFound('<h1>Specific models page crashed</h1>')
    
def reviews(request, model, slug):    
    try:
        brand = Brand.objects.get(name='Vivo')
        logging.debug(f"model: {slug}")
        logging.debug(f"brand: {brand}")
        brand_phones = PhoneModel.objects.filter(brand=brand)
        logging.debug(f"brand_phones: {brand_phones}")
        response = render(request, 'PhoneReview/specificModels.html', {'models': brand_phones})
        return HttpResponse(response)
    except:
        return HttpResponseNotFound('<h1>Review page crashed</h1>')