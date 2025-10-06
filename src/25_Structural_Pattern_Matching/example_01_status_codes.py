#!/usr/bin/env python

from enum import Enum

class StatusCodes(Enum):
    OK = 0
    NETWORK_ERROR = 1
    SYSTEM_ERROR = 2

status = StatusCodes.SYSTEM_ERROR
match status:
    case StatusCodes.OK:
        print("Operation completed successfully")
    case StatusCodes.NETWORK_ERROR:
        print("A network error has occurred")
    case StatusCodes.SYSTEM_ERROR:
        print("A system error has occurred")
    case _:
        print(f"Unknown status: {status}")

