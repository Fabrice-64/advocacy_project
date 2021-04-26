from .models import Region

def set_up_db():
    Region.objects.create(name="Grand-Est")
    Region.objects.create(name="Bretagne")