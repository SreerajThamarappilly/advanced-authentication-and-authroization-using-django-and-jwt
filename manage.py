# manage.py

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # This means Django isn't installed or there's an import error
        raise
    execute_from_command_line(sys.argv)
