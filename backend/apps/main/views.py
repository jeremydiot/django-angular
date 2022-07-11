from random import random
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['PUT'])
def random_float(request):
    return JsonResponse({'random': random()})
