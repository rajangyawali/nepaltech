from django.apps import AppConfig

class TechnologyConfig(AppConfig):
    name = 'technology'

    def ready(self):
        from crawler import updater
        updater.start()
    