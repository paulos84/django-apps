from .celery import app as celery_app

# This will make sure our Celery app is imported every time Django starts.
__all__ = ['celery_app']