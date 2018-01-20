from django.shortcuts import render
from django.views import generic
from .models import Person, Pet


class PersonListView(generic.ListView):
    model = Person
    context_object_name = 'person'
    template_name = 'person_list.html'

class PetListView(generic.ListView):
    model = Pet
    context_object_name = 'pet'

class PetDetailView(generic.DetailView):
    model = Pet
    context_object_name = 'pet'
