###################
# The entry point for our dartboard
# application. This should kick off all
# of the main processes of our application.
###################
from backend import django_setup
from Hub import Hub

import sys

# Note: this is used to make our workflows actually grab all the classes
# Some classes may not be directly called by our code and adding those
# to the extra_imports file allows those to be picked up by the installer
import extra_imports

# Opens a DartboardView window
# This should be the last thing executed here or should
# be moved to execute on it's own thread




if __name__ == "__main__":
    app = Hub()
    sys.exit(app.exec_())
