from django.apps import AppConfig


class {{cookiecutter.__project_titlecase}}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{cookiecutter.__package_name}}'
