A simple web based Django application for listing the 50 most recent tweets from @MapleRisk

Resource URLs:

http://127.0.0.1:8000/tweets/ List of the 50 most recent tweets

http://127.0.0.1:8000/map World map of countries associated with the tweets

http://127.0.0.1:8000/countries/ List of countries with their associated tweets


Getting Started
--------------

Prerequisites: Python 3.4, pip, virtualenv

After making and activating a virtual environment, run the following commands from the project's root directory:

    $ pip install -r requirements.txt

    $ python manage.py migrate

    $ python manage.py makemigrations app

    $ python manage.py migrate

    $ python manage.py shell


    >>> from app.models import Country, Tweet

    >>> Country.populate()

    >>> Tweet.get_tweets()

    >>> quit


    $ python manage.py runserver

The request made by get_tweets() requires OAuth authentication. Credentials are specified in the 'Tweet' model definition.

    >>> import requests
    >>> from requests_oauthlib import OAuth1

    >>> url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    >>> auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
    ...               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

    >>> requests.get(url, auth=auth)
    <Response [200]>
