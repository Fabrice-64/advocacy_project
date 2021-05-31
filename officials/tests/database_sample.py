from uuid import UUID
from officials import models as model
from interviews.models import Interview
from officials.calculations import OfficialRanking

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


ranking_sample = [
    OfficialRanking(first_name='Benoît', last_name='Lamy', id=UUID('4ec28643-11f5-42bc-bd15-ded5a6845305'), 
                    propinquity='8.44', qty_interviews=6, influence=2),
    OfficialRanking(first_name='Pauline', last_name='Pottier', id=UUID('eb3326b6-2a5f-4516-b7e5-cdf807717a72'), 
                    propinquity='2.59', qty_interviews=8, influence=31),
    OfficialRanking(first_name='Luce', last_name='Prevost', id=UUID('707a0ce1-62b7-4875-a8b9-49cf6efe6e54'), 
                    propinquity='4.05', qty_interviews=4, influence=30),
    OfficialRanking(first_name='Célina', last_name='Rey', id=UUID('1687784a-4e93-4d28-8c4d-b8d394fd2f49'), 
                    propinquity='3.58', qty_interviews=3, influence=32),
    OfficialRanking(first_name='Éric-Jean', last_name='Jourdan', id=UUID('31779db8-3084-4f71-bc33-257486efa1e5'), 
                    propinquity='1.39', qty_interviews=2, influence=6),
    OfficialRanking(first_name='Brigitte', last_name='Faure', id=UUID('9bcef3e3-4dee-42d1-97ba-962519be2d66'), 
                    propinquity='6.18', qty_interviews=4, influence=34),
    OfficialRanking(first_name='daisy-Éléonore', last_name='Neveu', id=UUID('99d921fa-9009-4774-b470-d88b68e645ea'), 
                    propinquity='9.83', qty_interviews=9, influence=9),
    OfficialRanking(first_name='Monique', last_name='de la Chartier', id=UUID('f5cfabd8-7416-473d-a5ed-51d321bce187'), 
                    propinquity='3.10', qty_interviews=1, influence=21),
    OfficialRanking(first_name='Margaud', last_name='Ledoux', id=UUID('47cc4d24-f248-4214-a81f-de1ed3281700'), 
                    propinquity='4.72', qty_interviews=1, influence=22),
    OfficialRanking(first_name='Marthe', last_name='Levy', id=UUID('abbbc6c7-c9a7-4099-818e-dd67f2fc07e9'), 
                    propinquity='4.34', qty_interviews=9, influence=13),
    OfficialRanking(first_name='Noémi', last_name='Richard', id=UUID('990f7a1c-7ea4-4711-9fa5-3e3a753a766f'), 
                    propinquity='9.67', qty_interviews=7, influence=28),
    OfficialRanking(first_name='Stéphane', last_name='Marion-Denis', id=UUID('bdf37d40-3b84-4380-847c-acc20b48003f'), 
                    propinquity='8.65', qty_interviews=4, influence=3),
    OfficialRanking(first_name='Frédérique', last_name='Marechal', id=UUID('e47bc178-01b7-4cba-aa12-657132709eb3'), 
                    propinquity='8.05', qty_interviews=8, influence=0),
    OfficialRanking(first_name='Thierry', last_name='Martineau de Vasseur', id=UUID('6e0b4d9d-05d6-46cd-bbda-66ad7828acd3'), 
                    propinquity='0.93', qty_interviews=6, influence=0),
    OfficialRanking(first_name='Yves', last_name='Bonnin', id=UUID('99206993-e7aa-43aa-9114-8954345d3182'), 
                    propinquity='6.12', qty_interviews=5, influence=15),
    OfficialRanking(first_name='Claire-Nathalie', last_name='Leleu', id=UUID('31e13344-0873-4bfb-bc91-bbcefff35781'), 
                    propinquity='7.30', qty_interviews=1, influence=12),
    OfficialRanking(first_name='Luc-Guy', last_name='Didier', id=UUID('4e6d597a-a3cb-4cd1-9cb6-8b6e5e5245ee'), 
                    propinquity='9.17', qty_interviews=3, influence=15),
    OfficialRanking(first_name='Julie', last_name='Laporte', id=UUID('8ffe37fb-08c6-45b9-9069-aded8e370359'), 
                    propinquity='8.03', qty_interviews=2, influence=34),
    OfficialRanking(first_name='Marine', last_name='Gay', id=UUID('de47efeb-50e7-4c5a-9bd1-addadea60af6'), 
                    propinquity='4.48', qty_interviews=1, influence=20),
    OfficialRanking(first_name='Chantal', last_name='Dupont', id=UUID('5bf87dc9-42f7-478a-890d-52404d636167'), 
                    propinquity='8.75', qty_interviews=7, influence=6)
]