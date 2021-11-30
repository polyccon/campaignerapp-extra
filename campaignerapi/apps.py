from django.apps import AppConfig


class WebservicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'campaignerapi'

     # def ready(self):
     #    # Import celery app now that Django is mostly ready.
     #    # This initializes Celery and autodiscovers tasks
     #    import campaignerapi.celery
