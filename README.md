# advocacy_project


## Tests:
## Commands for coverage and tests:
Using Shell, type the following command line:

$ coverage run --omit="venv/*,*/__init__.py,manage.py,*/tests.py,*/settings.py,*/migrations/*"  manage.py test
As one can see, all files and folders, which should not be subjects to tests have been removed.

And to get a report:
$ coverage report