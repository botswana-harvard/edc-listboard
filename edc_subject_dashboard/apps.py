from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edc_subject_dashboard'
    dashboard_template_name = None  # ??
