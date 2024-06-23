#!/usr/bin/env python
import os
import sys
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eattendance.settings')
    os.environ['MYSQL_PASSWORD']='tyui987$'
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    from attendance_marking_schedular import EventGenerator
    event_generator = EventGenerator()
    event_generator.startGeneratingEvents(time_between_event_cycles_in_seconds=300)


