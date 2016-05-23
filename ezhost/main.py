#!/usr/bin/python
"""
This module contains `main` method plus related subroutines.
`main` is executed as the command line ``ezhost`` program and takes care of
parsing options and commands

The other callables defined in this module are internal only. Anything useful
to individuals leveraging Fabric as a library, should be kept elsewhere.
"""
import sys

from ezhost.ServerLists import ServerLists
from ezhost.ServerLamp import ServerLamp

def main():
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