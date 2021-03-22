from django.apps import AppConfig


class BlogappConfig(AppConfig):
    name = 'blogapp'

    def ready(self):
        from . import signals