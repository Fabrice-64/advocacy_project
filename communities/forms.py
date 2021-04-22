from django.forms import ModelForm, ModelChoiceField
from django.shortcuts import render
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['intercom'].queryset = comms.Intercom.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['intercom'].queryset = comms.Intercom.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['intercom'].queryset = self.instance.department.intercom_set.order_by('name')    