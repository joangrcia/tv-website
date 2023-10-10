from django.apps import AppConfig


class SettingsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'settingsApp'
    label = 'qn_settings'

    def ready(self):
        import settingsApp.signals