from django.forms import ModelForm
from django.shortcuts import render
import communities.models as comms
from .ajax_functions import retrieve_departments_by_region, retrieve_intercoms_by_department


class RegionForm(ModelForm):
    class Meta:
        model = comms.Region
        fields = ['name']

class DepartmentForm(ModelForm):
    class Meta:
        model = comms.Department
        fields = ['region', 'name', 'dept_number']


class IntercomForm(ModelForm):
    class Meta:
        model = comms.Intercom
        fields = ['region', 'department', 'name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = comms.Department.objects.none()

        if 'region' in self.data:
            try:
                self.fields['department'].queryset = retrieve_departments_by_region(self.data)
            except (ValueError, TypeError):
                pass


class CityForm(ModelForm):
    class Meta:
        model = comms.City
        fields = ['region', 'department', 'intercom', 'name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = comms.Department.objects.none()
        self.fields['intercom'].queryset = comms.Intercom.objects.none()
        
        if 'region' in self.data:
            try:
                self.fields['department'].queryset = retrieve_departments_by_region(self.data)
            except (ValueError, TypeError):
                pass

        if 'department' in self.data:
            try:
                self.fields['intercom'].queryset = retrieve_intercoms_by_department(self.data)
            except (ValueError, TypeError):
                pass
