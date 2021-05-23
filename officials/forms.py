from django.forms import ModelForm
import officials.models as models
from django.forms import ModelForm, inlineformset_factory
from communities.models import Department, Intercom
from communities.ajax_functions import retrieve_intercoms_by_department, retrieve_city_by_department

class MandateInterComForm(ModelForm):
    class Meta:
        model = models.MandateInterCom
        fields = ['department', 'intercom', 'start_year', 'function']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['intercom'].queryset = Department.objects.none()

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
        self.fields['city'].queryset = Department.objects.none()

        if 'department' in self.data:
            try:
                self.fields['city'].queryset = retrieve_city_by_department(self.data)
            except (ValueError, TypeError):
                pass