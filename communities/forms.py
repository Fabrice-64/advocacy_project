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
        fields = ['region', 'department', 'name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = comms.Department.objects.none()

        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['department'].queryset = comms.Department.objects.filter(region_id=region_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['department'].queryset = self.instance.region.department_set.order_by('name')    


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
                region_id = int(self.data.get('region'))
                self.fields['department'].queryset = comms.Department.objects.filter(region_id=region_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['department'].queryset = self.instance.region.department_set.order_by('name')

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['intercom'].queryset = comms.Intercom.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['intercom'].queryset = self.instance.region.department.intercom_set.order_by('name')
            self.fields['intercom'].queryset = self.instance.department.intercom_set.order_by('name')
