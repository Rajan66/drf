from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict
import json

def api_home(request,*args, **kwargs):
    body = request.body
    print(request.GET) # url query params
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)


def api_products(request,*args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    # if model_data:
    #     data["id"] = model_data.id
    #     data['title'] = model_data.title
    #     data['content'] = model_data.content
    #     data['price'] = model_data.price
        # model_instance (model_data)
        # turn it into a python dict
        # return JSON to the client who requested the API
        # this is what we tried to do above
        
    if model_data:
        data= model_to_dict(model_data,fields=['id','title'])
    return JsonResponse(data)