#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


<<<<<<< HEAD

=======
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whiptobar.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


<<<<<<< HEAD
=======



>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
if __name__ == '__main__':
    main()
