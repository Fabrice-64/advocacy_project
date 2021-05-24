from django.forms import ModelForm
import officials.models as models
from django.forms import ModelForm
from communities.models import Department, Intercom, City
from communities.ajax_functions import retrieve_intercoms_by_department, retrieve_city_by_department

class MandateInterComForm(ModelForm):
    class Meta:
        model = models.MandateInterCom
        fields = ['department', 'intercom', 'start_year', 'function']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['intercom'].queryset = Intercom.objects.none()

        if 'department' in self.data:
            try:
                self.fields['intercom'].queryset = retrieve_intercoms_by_department(self.data)
            except (ValueError, TypeError):
                pass


class MandateCityForm(ModelForm):
    class Meta:
        model = models.MandateCity
        fields = ['department', 'city', 'start_year', 'function']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'department' in self.data:
            try:
                self.fields['city'].queryset = retrieve_city_by_department(self.data)
            except (ValueError, TypeError):
                pass

import django.forms as forms
from communities.models import Department
from .models import MandateCity
class OfficialCreationForm(ModelForm):
    departments = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="--------",
    blank=True, required=False)
    class Meta:
        model = models.Official
        fields = ['departments', 'first_name', 'last_name', 'mandate_city', 
                'mandate_intercom', 'mandate_department', 'mandate_region', 
                'mp_mandate', 'senator_mandate']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mandate_city'].queryset = MandateCity.objects.none()