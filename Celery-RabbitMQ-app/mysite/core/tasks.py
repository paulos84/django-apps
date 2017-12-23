import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

# create a Celery task that generates a number of random User accounts.

@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)

"""
from celery import shared_task

@shared_task
def name_of_your_function(optional_param):
    pass  # do something heavy
"""