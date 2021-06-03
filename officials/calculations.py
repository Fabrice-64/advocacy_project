"""
    This modules calculates the influence and propinquity of an official.

    The influence calculation relies on a simple equation:
    number of mandates x level of the mandate.
    the sum of all mandates gives the level of influence.

    INFLUENCE_INDEX:
    Each level of electoral mandate is rated.
    Future versions may include the size of the community, its GDP and the function of the official.

    The propinquity is the proximity of ideas.
    In the current version the proximity of ideas is expressed in the assessment of interviews.
    Further versions may include political statements, press interviews and exploit NLP Possibilities.

    Functions:
    def interview_propinquity:
        calculate this propinquity

    def calculate_ranking:
        attribute:
            list of officials, issued from a query in the view officials_ranking
        returns:
            list of named tuples containing first_name, last_name, id, propinquity, number of interviews and influence
            of every official.

"""
from collections import namedtuple
from officials import models as model
from interviews.models import Interview

INFLUENCE_INDEX = {
    "city_idx": 1,
    "intercom_idx": 2,
    "department_idx": 3,
    "region_idx": 4,
    "mp_idx": 5,
    "senator_idx": 5
}

OfficialRanking = namedtuple("OfficialRanking", "first_name last_name id propinquity  qty_interviews influence")


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


def influence_calculation(official_id):
    city_influence = city_influence_calculation(official_id)
    intercom_influence = intercom_influence_calculation(official_id)
    department_influence = department_influence_calculation(official_id)
    region_influence = region_influence_calculation(official_id)
    mp_influence = mp_influence_calculation(official_id)
    senator_influence = senator_influence_calculation(official_id)
    # Influence is the sum of all recorded electoral mandates.
    total_influence = city_influence + intercom_influence + department_influence \
        + department_influence + region_influence + mp_influence + senator_influence
    return total_influence


def interview_propinquity(id):
    interviews = Interview.objects.filter(official__id=id)
    itw_propinquity = 0
    for interview in interviews:
        if len(interviews) > 0:
            if interview.assessment == "TBD":
                itw_propinquity += 0
            elif interview.assessment == "0PC":
                itw_propinquity -= -5
            elif interview.assessment == "25PC":
                itw_propinquity += 2
            elif interview.assessment == "50PC":
                itw_propinquity += 5
            elif interview.assessment == "75PC":
                itw_propinquity += 7
            else:
                itw_propinquity += 10
    if len(interviews) > 0:
        itw_propinquity = itw_propinquity / len(interviews)
    return itw_propinquity, len(interviews)


def propinquity_calculation(id):
    """
        In V1 only interviews are taken into account
    """
    itw_propinquity, qty_interviews = interview_propinquity(id)
    return itw_propinquity, qty_interviews


def importance_summary(id, first_name, last_name):
    """
        Collects the influence and propinquity of an official

        Returns:
            a named tuple of the official with his first_name, last_name, id,
            propinquity, number of interviews and influence.
    """
    influence = influence_calculation(id)
    propinquity, qty_interviews = propinquity_calculation(id)

    return OfficialRanking(
        first_name, last_name,
        id, propinquity, qty_interviews, influence)


def calculate_ranking(officials):
    """
        Allows the views:
        officials_ranking
        officials_to_engage
        to display the assessed importance of offcials.

        Returns:
            a list of named tuples.
    """
    officials_list = list()
    for official in officials:
        official_ranking = importance_summary(
            official.id,
            official.first_name,
            official.last_name)
        officials_list.append(official_ranking)
    return officials_list
