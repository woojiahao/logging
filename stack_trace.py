import logging

try:
    a = 10 / 0
except Exception as exc:
    logging.critical("Critical error occurred")

try:
    a = 10 / 0
except Exception as exc:
    logging.critical("Critical error occurred", exc_info=True)
