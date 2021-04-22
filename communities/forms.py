from django.forms import ModelForm, ModelChoiceField
import communities.models as comms



class RegionForm(ModelForm):
    class Meta:
        model = comms.Region
        fields = ['name']

class DepartmentForm(ModelForm):
    class Meta:
        model = comms.Department
        fields = ['name', 'dept_number', 'region']

class IntercomForm(ModelForm):
    class Meta:
        model = comms.Intercom
        fields = ['name', 'department']


class CityForm(ModelForm):
    class Meta:
        model = comms.City
        fields = ['name', 'department', 'intercom']