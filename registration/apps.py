from django.apps import AppConfig


class RegistrationsConfig(AppConfig):
    name = 'registration'

    def ready(self):
        import registration.signals