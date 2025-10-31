##################
# This contains any functions necessary to setup
# and configure django. This should only be called
# once at the very beginning of execution.
##################
import django
from django.core.management import call_command
from django.conf import settings
from pathlib import Path


##
# Basic setup function for the backend. This automatically configures
# django and migrates the database to the latest version
def setup():
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    base_dir = Path(__file__).resolve().parent.parent

    # Configuration for the Database.
    db_config = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': base_dir / 'db.sqlite3',
        }
    }

    # Configuration for installed applications (right now just the datamodel)
    apps = [
        'backend.apps.BackendConfig'
    ]

    # Apply the settings and initialize django
    if not settings.configured:
        settings.configure(DEBUG=True, DATABASES=db_config, INSTALLED_APPS=apps)
        django.setup()

    # Update the database
    call_command("migrate")


setup()
