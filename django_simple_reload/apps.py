from django.apps import AppConfig


class AutoReloadConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_simple_reload"
    verbose_name = "Django Auto Reload"
