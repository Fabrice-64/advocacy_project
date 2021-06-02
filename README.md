# Avocacy Project For Charities

## Disclaimer
The legal framework of this application has not been validated. Therefore it should be used exclusively for development purpose.
Any organization which would like to make use of it should first get the approval of a lawyer.

## Why this project ?
Along with their support to the people, Charities aim at advocating their cause to the officials and other stakeholders.  
This project, conceived in the framework of an OpenClassrooms education programm as software developer, intends to provide
those charities with a convenient tool which helps them to engage officials with the support of Volunteers.

## Limitations
The current limitations of this project are:
- A community organization exclusively bound to France continental territory
- Limitations in the design restraint its use to local charities. It is not suitable for large organizations in its current format.
- Password Reset, User deactivation are not available in this V1.
- Only elected officials are taken into consideration.

## Main functionalites
- The account creation follows a specific process:
    * The administrator should create the first manager;
    * The manager owns the permission to create new users;
    * Once created a new user receives an e-mail, which includes a unique usage link;
    * The user is expected to click on this link;
    * Then the user will access a page where he is requested to change the password;
    * As he changes his password, he automatically get the permissions depending on his status 
    and he is logged in.
- Managers can create new communities and officials
- Managers can add advocacy topics in order to help the volunteers focus on the message.
- Managers set up interview guidelines as support documentation for the volunteers.
- Volunteers can report on the outcome of any interview. This outcome is used to assess the propinquity of the officials.
- Officials are sorted out in 4 categories:  
    * Influential and Ideas close to the charity ideals  
    * Less Influential and Ideas close to the charity ideals  
    * Influential and Ideas rather far from the charity ideals  
    * Less Influential and Ideas rather far from the charity ideals 
- An additional page gives the list of the officials to meet. That is: those with a certain relevance and at a reasonable
distance from the charity ideals. The officials who have not been interviewed do not belong to this list, as their propinquity was never
assessed.  
**In order to respect the freedom of thinking and speech, nowhere in the application is recorded what the ideas of the official are**

## Versions
V1.1 : beta, with developed graphic interface. To be published.
V1.0 : beta, fully functionnal. Published on 2. June 2021

## Tests:
### Test Coverage
This project has been largely develop in TDD mode. 
Coverage rate is at 96%.  
### Locate the tests
Every app has its own unitary tests.  
DB fixtures are located in the `pages` app.
Selenium tests can be found in the `advocacy_project` module.
### Commands for coverage and tests:
Using Shell, type the following command line:  
`$ coverage run --omit="venv/*,*/__init__.py,manage.py,*/tests.py, */test*,*/settings.py,*/migrations/*"  manage.py test`  
As one can see, all files and folders, which should not be subjects to tests have been removed.  
And to get a report:  
`$ coverage report`
## Create fixtures
Would a developer have the intent to build his own fixtures, the amount of dependencies between the tables demand to apply the following
code:
``` python manage.py dumpdata auth.Group -e contenttypes  --natural-foreign --indent 2 > groups.json```

## Database
### DB Used
PostgreSQL is the DB used in this project.

### Initialize the Database
As Usual, first comes first with the creation of a superuser.
After Migration, the DB initialization DB should follow this order:
- Upload the Groups from the `permissions_and_groups` folder. The Groups specificic to this project are implemented in this file.
- Create some communities;
- Create the teams for the Volunteers;
- Create the Volunteers or Staff of the charity;
- Create Officials;
- Create interviews on case by case basis.
This project includes a folder with the standard permissions and groups.  
It is named: `permissions_and_groups`. It can be found at the root of this project.
## Third party packages
Beyond Django, following third party packages are used:
- django-registration-redux, used to manage the account creation and authentication process;
- pandas, used to compute the officials level of influence and propinquity;
- selenium, to test the User Stories;
- psycopg2-binary, for Postgresql;  
Those packages are all referred to in `requirements.txt`.





