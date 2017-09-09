from django.views.generic.base import TemplateView
from django.http import JsonResponse

def base_view(req):
    return JsonResponse({'foo': 'bar'})
