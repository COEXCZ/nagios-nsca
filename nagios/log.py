import logging
import nagios

MAP_LEVEL_NAGIOS = {
    logging.DEBUG: nagios.OK,
    logging.INFO: nagios.OK,
    logging.WARNING: nagios.WARNING,
    logging.ERROR: nagios.WARNING,
    logging.CRITICAL: nagios.CRITICAL,
}

class NagiosHandler(logging.Handler):
    def emit(self, record):
        nagios.send(record.message, service_status=MAP_LEVEL_NAGIOS[record.levelno])
