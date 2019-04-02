import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Animal

def animal_list(request):
    animals = [
        a for a in Animal.objects.all().values(
            'name', 'specie', 'gender',
            'age', 'size','hair', 'color',
            'description', 'address'
        )
    ]

    return JsonResponse(
        animals, safe=False
    )

@csrf_exempt
def animal_add(request):
    if request.method == 'POST':
        animal = json.loads(
            request.body.decode('utf-8')
        )

    a = Animal(
        name=animal['name'],
        specie=animal['specie'],
        gender=animal['gender'],
        age=animal['age'],
        size=animal['size'],
        hair=animal['hair'],
        color=animal['color'],
        description=animal['description'],
        address=animal['address']
    )
    a.save()

    return JsonResponse(
        animal, safe=False
    )

