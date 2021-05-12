from communities.models import Department, Intercom

def retrieve_departments_by_region(data):
    region_id = int(data.get('region'))
    return Department.objects.filter(region_id=region_id).order_by('name')

def retrieve_intercoms_by_department(data):
    department_id = int(data.get('department'))
    return Intercom.objects.filter(department_id=department_id).order_by('name')