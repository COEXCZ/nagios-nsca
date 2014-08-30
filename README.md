nagios-nsca
===========

Nagios passive checks support for Python (and Django).

License
-------
OSI Approved - GNU Lesser General Public License v3 (LGPLv3)

Installation
------------

```bash
$ pip install nagios-nsca
```

Basic usage
-----------

    from nagios import send_warning
    send_warning('Something is wrong there.')
    
Available functions
-------------------

    send(message, 
        nsca=NSCA, 
        target_host=TARGET_HOST, 
        host_name=HOST_NAME, 
        service_description=SERVICE_DESCRIPTION, 
        service_status=OK)


    send_ok(message,
        nsca=NSCA,
        target_host=TARGET_HOST,
        host_name=HOST_NAME,
        service_description=SERVICE_DESCRIPTION)


    send_warning(message,
        nsca=NSCA,
        target_host=TARGET_HOST,
        host_name=HOST_NAME,
        service_description=SERVICE_DESCRIPTION)


    send_critical(message,
        nsca=NSCA,
        target_host=TARGET_HOST,
        host_name=HOST_NAME,
        service_description=SERVICE_DESCRIPTION)


    send_unknown(message,
        nsca=NSCA,
        target_host=TARGET_HOST,
        host_name=HOST_NAME,
        service_description=SERVICE_DESCRIPTION)

Integration within Django
-------------------------

settings.py:

    NAGIOS_NSCA = "/usr/sbin/send_nsca"
    NAGIOS_TARGET_HOST = "nagios.coex.cz"
    NAGIOS_HOST_NAME = ""
    NAGIOS_SERVICE_DESCRIPTION = ""
    NAGIOS_DISABLED = False

logging module:

    LOGGING = {
        ...
        'handlers': {
            ...
            'nagios': {
                'level': 'CRITICAL',
                'class': 'nagios.log.NagiosHandler'
            }
        },
        'loggers': {
            ...
            'project': {
                'handlers': [..., 'nagios'],
                'level': 'INFO',
            },
        },
    }
