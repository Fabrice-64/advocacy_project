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
   OfficialRanking(first_name='Josette', last_name='Germain-Garnier', id=UUID('6563dfd9-ea9d-443d-bf91-b9a5f9808e41'), propinquity=8.44, qty_interviews=6, influence=2),
 OfficialRanking(first_name='Françoise', last_name='Faivre', id=UUID('58e8442a-623a-4230-ad17-5963f3db170e'), propinquity=2.59, qty_interviews=8, influence=31),
 OfficialRanking(first_name='Benjamin', last_name='Le Coulon', id=UUID('6bac3e8e-664f-4c83-bf55-4fd3f4b62385'), propinquity=4.05, qty_interviews=4, influence=30),
 OfficialRanking(first_name='Stéphane', last_name='Camus-Hardy', id=UUID('99aca2eb-bc6a-49df-adad-612aee4e1763'), propinquity=3.58, qty_interviews=3, influence=32),
 OfficialRanking(first_name='Raymond', last_name='Rolland', id=UUID('f85c4bec-abbe-401a-91b0-5bc25f4896a6'), propinquity=1.39, qty_interviews=2, influence=6),
 OfficialRanking(first_name='Patrick', last_name='Leblanc', id=UUID('5766b965-3ac8-496f-89f0-0c942f13a3c5'), propinquity=6.18, qty_interviews=4, influence=34),
 OfficialRanking(first_name='Nathalie', last_name='Morin', id=UUID('1f7f714a-d5b9-43fa-9fc1-111e67bb0533'), propinquity=9.83, qty_interviews=9, influence=9),
 OfficialRanking(first_name='Suzanne', last_name='Perrot', id=UUID('67e51c9d-c710-4ff3-9536-8539407847ed'), propinquity=3.1, qty_interviews=1, influence=21),
 OfficialRanking(first_name='Thibaut-Honoré', last_name='Pottier', id=UUID('0dc2fd42-f156-4d28-8da0-dfb12e5d944e'), propinquity=4.72, qty_interviews=1, influence=22),
 OfficialRanking(first_name='Julie', last_name='Etienne de Mendes', id=UUID('e60e7aa0-154e-45f3-8f7f-b2e0b01677d9'), propinquity=4.34, qty_interviews=9, influence=13),
 OfficialRanking(first_name='Victoire', last_name='du Marty', id=UUID('ee34208c-651b-4ae1-9155-a0b815746bdf'), propinquity=9.67, qty_interviews=7, influence=28),
 OfficialRanking(first_name='Nicolas', last_name='Chevallier', id=UUID('045fa701-8e13-42e8-b519-4947fd4ed9c1'), propinquity=8.65, qty_interviews=4, influence=3),
 OfficialRanking(first_name='Caroline', last_name='de Techer', id=UUID('11d79c44-8d59-4b2d-8dab-d04aacd6012d'), propinquity=8.05, qty_interviews=8, influence=0),
 OfficialRanking(first_name='Zoé', last_name='Barbier', id=UUID('4b110e02-cc31-4f0b-b9db-7c2fc795ec75'), propinquity=0.93, qty_interviews=6, influence=0),
 OfficialRanking(first_name='Richard', last_name='Millet', id=UUID('43e39aa8-ae71-4b43-b9d5-2b0dd0675d03'), propinquity=6.12, qty_interviews=5, influence=15),
 OfficialRanking(first_name='Alphonse', last_name='Chauvin', id=UUID('1dac27f4-5cf1-440d-b01f-c376539e8ef1'), propinquity=7.3, qty_interviews=1, influence=12),
 OfficialRanking(first_name='Alain', last_name='Petit Le David', id=UUID('bfa0b05c-47d3-48a3-a7e1-227cd323b5cf'), propinquity=9.17, qty_interviews=3, influence=15),
 OfficialRanking(first_name='Michel', last_name='de Masson', id=UUID('e17a6c77-8d3b-4837-87f2-ff1278b74fcb'), propinquity=8.03, qty_interviews=2, influence=34),
 OfficialRanking(first_name='Édouard', last_name='Le Goff-Lagarde', id=UUID('5544cb44-8389-43a6-bf83-11dc6cea74bb'), propinquity=4.48, qty_interviews=1, influence=20),
 OfficialRanking(first_name='Alexandre', last_name='Robert', id=UUID('fa8f5c49-49ca-4afc-ac00-d141055d86b8'), propinquity=8.75, qty_interviews=7, influence=6)
]