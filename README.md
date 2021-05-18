# advocacy_project


## Tests:
## Commands for coverage and tests:
Using Shell, type the following command line:

$ coverage run --omit="venv/*,*/__init__.py,manage.py,*/tests.py, */test*,*/settings.py,*/migrations/*"  manage.py test
As one can see, all files and folders, which should not be subjects to tests have been removed.

And to get a report:
$ coverage report

## Initialize the Database
To be written

## Tests
### Fixtures
The project structure demands very accurate fixture configuration. <br>
To get excerpts of a DB, please dump the data as such:
```
$ python manage.py dumpdata auth.Group -e contenttypes  --natural-foreign --indent 2 > groups.json
```
