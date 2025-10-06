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
    case StatusCodes.NETWORK_ERROR | StatusCodes.SYSTEM_ERROR:
        print("An error has occurred")
    case _:
        print(f"Unknown status: {status}")


