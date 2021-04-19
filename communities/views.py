from django.shortcuts import render
from django.views.generic import ListView
from django_oso.auth import authorize

# Create your views here.
from communities.models import Region

def communities(request):
    return render(request, "communities/communities.html")

class RegionsListView(ListView):
    model = Region

    def get_queryset(self):
        return Region.objects.authorize(self.request, action="read")
    
    