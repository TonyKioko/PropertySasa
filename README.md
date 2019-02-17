PropertySasa
===================
## Description
[PropertySasa](https://propertysasa.herokuapp.com/) is a web application that seeks to connect property owners with buyers.

------------------------------------------------------------------------

## User Requirements

1. Post Properties.
2. View all posted properties.
3. Search for property by Location, Price and City.
4. Contact Property owners

### Live Link ###
[PropertySasa](https://propertysasa.herokuapp.com/)
## Getting started

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python3.6

### Cloning the repository
```bash
git clone https://github.com/TonyKioko/PropertySasa && cd PropertySasa
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip3 install -r requirements
```

### Prepare environmet variables
For this project you will need the following configurations plus email setup for email registration hmac verification.
```python
SECRET_KEY= #secret key will be added by default
DEBUG= #set to false in production
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD=#database password
DB_HOST="127.0.0.1"
MODE= # dev or prod , set to prod during production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

### Database migrations

```bash
python manage.py migrate
```

### Running the server
```bash
python manage.py runserver
```

### Admin Dashboard
Use django admin to manage the different users and posts.

### Deploying to heroku
Refer to this guide: [deployment to heroku](https://github.com/Benard18/Deployment_to_heroku_django)

## Running the tests
```bash
python manage.py app test
```

## Live Demo

The web app can be accessed from the following link:
[PropertySasa](https://propertysasa.herokuapp.com/)

## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)

## Test Driven Development
* Testing was done using python inbuild test tool called unittest


## Known Bugs
There are no known bugs.

## License ([MIT License](http://choosealicense.com/licenses/mit/))
This project is licensed under the MIT Open Source license,Copyright (c) 2018 [Tony Kioko](https://github.com/tonykioko/)
