from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
import communities.models as comms

class RegionsListView(ListView):
    model = comms.Region
    