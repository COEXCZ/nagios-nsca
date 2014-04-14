# -*- coding: utf-8 -*-
"""
Library for sending notifications to Nagios using 'send_nsca' command.
"""

__all__ = (
    "send_ok", "send_warning", "send_warning", "send_critical",
)


from subprocess import Popen, PIPE

OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

settings = None
try:
    from django.conf import settings
except ImportError:
    pass

NSCA = getattr(settings, "NAGIOS_NSCA", "/usr/sbin/send_nsca")
TARGET_HOST = getattr(settings, "NAGIOS_TARGET_HOST", "nagios.coex.cz")
HOST_NAME = getattr(settings, "NAGIOS_HOST_NAME", "")
SERVICE_DESCRIPTION = getattr(settings, "NAGIOS_SERVICE_DESCRIPTION", "")
DISABLED = getattr(settings, "NAGIOS_DISABLED", False)


def send(message,
         nsca=NSCA,
         target_host=TARGET_HOST,
         host_name=HOST_NAME,
         service_description=SERVICE_DESCRIPTION,
         service_status=OK):
    line = "%s\t%s\t%d\t%s\n" % (host_name, service_description, service_status, message)
    if DISABLED:
        print line.decode("utf-8")
        return False
    pipe = Popen((nsca, target_host), stdin=PIPE)
    pipe.communicate(line)
    pipe.stdin.close()
    pipe.wait()
    return True


def send_ok(message,
            nsca=NSCA,
            target_host=TARGET_HOST,
            host_name=HOST_NAME,
            service_description=SERVICE_DESCRIPTION):
    return send(message, nsca, target_host, host_name, service_description, OK)


def send_warning(message,
                 nsca=NSCA,
                 target_host=TARGET_HOST,
                 host_name=HOST_NAME,
                 service_description=SERVICE_DESCRIPTION):
    return send(message, nsca, target_host, host_name, service_description, WARNING)


def send_critical(message,
                  nsca=NSCA,
                  target_host=TARGET_HOST,
                  host_name=HOST_NAME,
                  service_description=SERVICE_DESCRIPTION):
    return send(message, nsca, target_host, host_name, service_description, CRITICAL)


def send_unknown(message,
                 nsca=NSCA,
                 target_host=TARGET_HOST,
                 host_name=HOST_NAME,
                 service_description=SERVICE_DESCRIPTION):
    return send(message, nsca, target_host, host_name, service_description, UNKNOWN)
