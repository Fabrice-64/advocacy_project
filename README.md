# advocacy_project


## Tests:
## Commands for coverage and tests:
Using Shell, type the following command line:

$ coverage run --omit="venv/*,*/__init__.py,manage.py,*/tests.py,*/tests_*, */test*,*/settings.py,*/migrations/*"  manage.py test
As one can see, all files and folders, which should not be subjects to tests have been removed.

And to get a report:
$ coverage report

## Initialize the Database
*** Remark : The following remarks may be no more valid, as this project is a work in progress. *** <br>
Therefore, first try and install the project as recommended by Django and if it does not work, 
the following process should.<br>
The CustomUser model includes a foreign key by which a team is assigned to a new user.
Therefore, for the first use of this project, you should initialize the DB using the CLI.

Here is the process depicted in detail:

First of all, switch to the project folder and activate the virtual environment.
Then:

$ python manage.py shell
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
```
>>> from communities.models import Region, Department, Intercom, City
>>> from teams.models import Team
>>> region = Region.objects.create(name="Grand-Est")
>>> department = Department.objects.create(name="Bas-Rhin", dept_number="67", region=region)
>>> intercom = Intercom.objects.create(name="Strasbourg Eurométropole", department=department, region=region)
>>> city = City.objects.create(name="Strasbourg", intercom=intercom, department=department, region=region)
>>> team = Team.objects.create(name="Salariés", city=city)
>>> user = CustomUser.objects.create_user(username="fabricejaouen", password="admin", team=team)
>>> user.is_superuser=True
>>> user.is_active=True
>>> user.is_staff=True
>>> user.first_name="Fabrice" # Don't forget to specify the first name: it will make changes possible.
>>> user.save()
```

Then, you exit python, and type:

$ python manage.py createsuperuser

## Tests
### Fixtures
The project structure demands very accurate fixture configuration. <br>
To get excerpts of a DB, please dump the data as such:
```
$ python manage.py dumpdata auth.Group -e contenttypes  --natural-foreign --indent 2 > groups.json
```
