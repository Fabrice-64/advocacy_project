from django.forms import ModelForm
import communities.models as comms



class RegionForm(ModelForm):
    class Meta:
        model = comms.Region
        fields = ['name']
