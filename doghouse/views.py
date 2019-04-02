import json

from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Animal

def animal_list(request):
    animals = [
        a for a in Animal.objects.all().values()
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

@csrf_exempt
def animal_remove(request, id):
    if request.method == 'DELETE':
        status = None
        try:
            animal = get_object_or_404(Animal, id=id)
            animal.delete()
            status = 'deleted'
        except Http404:
            status = 'animal not found'
        finally:
            return JsonResponse({'status': status})

