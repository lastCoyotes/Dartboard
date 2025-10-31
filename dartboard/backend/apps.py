###################
# This is a basic app configuration
# to allow django to detect that the
# backend actually exists here.
###################
from django.apps import AppConfig


##
# Defines the configuration of the backend for django
class BackendConfig(AppConfig):
    name = 'backend'
    verbose_name = "Dartboard Backend"
