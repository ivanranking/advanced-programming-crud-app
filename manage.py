#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ap_capstone.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? "
            "You may need to install Django with 'pip install Django'."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
