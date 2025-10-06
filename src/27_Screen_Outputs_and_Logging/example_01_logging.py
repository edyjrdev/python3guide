#!/usr/bin/env python

import logging

logging.basicConfig(
    filename="program.log",
    level=logging.DEBUG,
    style="{",
    format="{asctime} [{levelname:8}] {message}",
    datefmt="%d.%m.%Y %H:%M:%S")

logging.error("An error has occurred")
logging.info("This is information")
logging.error("And another error")
