from django.db import models

class Animal(models.Model):

    specie_choice = (('cat', 'gato'), ('dog', 'cachorro'))
    gender_choice = (('female', 'fêmea'), ('male', 'macho'))
    age_choice = (
        ('kitten', 'filhote'), ('young', 'jovem'),
        ('adult', 'adulto'), ('senior', 'idoso'),
    )
    size_choice = (
        ('small', 'pequeno'), ('medium', 'médio'), ('large', 'grande')
    )
    hair_choice = (('short', 'curto'), ('medium', 'médio'), ('long', 'longo'))

    name = models.CharField(max_length=20)
    specie = models.CharField(max_length=10, choices=specie_choice)
    gender = models.CharField(max_length=10, choices=gender_choice)
    age = models.CharField(max_length=10, choices=age_choice)
    size = models.CharField(max_length=10, choices=size_choice)
    hair = models.CharField(max_length=10, choices=hair_choice)
    color = models.CharField(max_length=20)
    description_ = models.TextField()
    address = models.CharField(max_length=25)

