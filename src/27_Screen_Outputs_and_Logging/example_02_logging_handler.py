#!/usr/bin/env python

import logging
import sys

handler = logging.StreamHandler(sys.stdout)
frm = logging.Formatter("{asctime} {levelname}: {message}", "%d.%m.%Y %H:%M:%S", style="{")
handler.setFormatter(frm)

logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.critical("A really critical error")
logger.warning("And a subsequent warning")
logger.info("This, on the other hand, is just for your information")

