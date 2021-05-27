from officials import models as model

INFLUENCE_INDEX = {
    "city_idx" : 1,
    "intercom_idx": 2,
    "department_idx": 3,
    "region_idx": 4,
    "mp_idx": 5,
    "senator_idx": 5
}

def city_influence_calculation(official_id):
    nb_mandates = model.MandateCity.objects.filter(official__id=official_id).count()
    return nb_mandates * INFLUENCE_INDEX.get("city_idx")

def intercom_influence_calculation(official_id):
    nb_mandates = model.MandateInterCom.objects.filter(official__id=official_id).count()
    return nb_mandates * INFLUENCE_INDEX.get("intercom_idx")
    
def department_influence_calculation(official_id):
    nb_mandates = model.MandateDepartment.objects.filter(official__id=official_id).count()
    return nb_mandates * INFLUENCE_INDEX.get("department_idx")

def region_influence_calculation(official_id):
    nb_mandates = model.MandateRegion.objects.filter(official__id=official_id).count()
    return nb_mandates * INFLUENCE_INDEX.get("region_idx")

def mp_influence_calculation(official_id):
    nb_mandates = model.MPMandate.objects.filter(official__id=official_id).count()
    return nb_mandates * INFLUENCE_INDEX.get("mp_idx")

def senator_influence_calculation(official_id):
    nb_mandates = model.SenatorMandate.objects.filter(official__id=official_id).count()
    return nb_mandates * INFLUENCE_INDEX.get("senator_idx")

from collections import namedtuple
from interviews.models import Interview
OfficialRanking = namedtuple("OfficialRanking", "first_name last_name id propinquity influence")

def influence_calculation(official_id):
    city_influence = city_influence_calculation(official_id)
    intercom_influence = intercom_influence_calculation(official_id)
    department_influence = department_influence_calculation(official_id)
    region_influence = region_influence_calculation(official_id)
    mp_influence = mp_influence_calculation(official_id)
    senator_influence = senator_influence_calculation(official_id)

    total_influence = city_influence + intercom_influence + department_influence \
        + department_influence + region_influence + mp_influence + senator_influence
    return total_influence

def propinquity_calculation(id):
    interviews = Interview.objects.filter(official__id=id)
    propinquity = 0
    for interview in interviews:
        if len(interviews) > 0:
            if interview.assessment == "TBD":
                propinquity += 0
            elif interview.assessment == "GOAL_0_PC":
                propinquity -= 5
            elif interview.assessment == "GOAL_25_PC":
                propinquity += 2
            elif interview.assessment == "GOAL_50_PC":
                propinquity += 5
            else:
                propinquity += 10
    if len(interviews) > 0:
        propinquity = propinquity/ len(interviews)
    return propinquity

def importance_summary(id, first_name, last_name):
    influence = influence_calculation(id)
    propinquity= propinquity_calculation(id)

    return OfficialRanking(first_name, last_name, 
        id, propinquity, influence)

def calculate_ranking():
    officials_list = list()
    officials = model.Official.objects.all()
    for official in officials:
        official_ranking = importance_summary(official.id,
        official.first_name, official.last_name)
        officials_list.append(official_ranking)
    return officials_list
