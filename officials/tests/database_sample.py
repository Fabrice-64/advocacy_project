from officials import models as model
from interviews.models import Interview

def setup_sample_database():
    model.Official.objects.bulk_create([
            model.Official(first_name="official1", last_name="name_official1"),
            model.Official(first_name="official2", last_name="name_official2")
        ])
    model.MPMandate.objects.create(start_year=2020)
    model.SenatorMandate.objects.create(start_year=2020)
    model.MandateRegion.objects.create(start_year=2020)
    model.MandateDepartment.objects.create(start_year=2020)
    model.MandateInterCom.objects.create(start_year=2020)
    model.MandateCity.objects.create(start_year=2020)


    off1 = model.Official.objects.get(first_name="official1")
    off2 = model.Official.objects.get(first_name="official2")

    mp_mandate = model.MPMandate.objects.get(start_year=2020)
    senator_mandate = model.SenatorMandate.objects.get(start_year=2020)
    mandate_region = model.MandateRegion.objects.get(start_year=2020)
    mandate_department = model.MandateDepartment.objects.get(start_year=2020)
    mandate_intercom = model.MandateInterCom.objects.get(start_year=2020)
    mandate_city = model.MandateCity.objects.get(start_year=2020)

    off1.mp_mandate.set([mp_mandate])
    off1.mandate_region.set([mandate_region])
    off1.mandate_intercom.set([mandate_intercom])
    off1.mandate_city.set([mandate_city])

    off2.senator_mandate.set([senator_mandate])
    off2.mandate_department.set([mandate_department])
    off2.mandate_intercom.set([mandate_intercom])
    off2.mandate_city.set([mandate_city])

    Interview.objects.create(assessment="25PC", official=off1)
    Interview.objects.create(assessment="100PC", official=off1)