from django.apps import AppConfig


class EycaConfig(AppConfig):
    name = 'eyca'

    def ready(self):
        import eyca.signals
