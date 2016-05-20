#!/usr/bin/python
import sys

from ServerLists import ServerLists
from ServerLamp import ServerLamp

"""
Check args
"""
try:
    arg1 = sys.argv[0]
    arg2 = sys.argv[1]
    server = ServerLists(arg2)
except Exception as e:
    raise e

"""
Call server install function
"""
eval(server.name)().install()



