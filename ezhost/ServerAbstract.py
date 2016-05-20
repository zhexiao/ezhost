# -*- coding: utf-8 -*-
"""
Abstract class for all server class
"""

# internal libs
from abc import ABCMeta, abstractmethod
import os

# fabric libs
from fabric.colors import red, green
from fabric.api import env, prompt, run, sudo, local, put
from fabric.contrib.files import exists
from fabric.state import output

# hide exec command
output['running'] = False

class ServerAbstract(metaclass=ABCMeta):
    @abstractmethod
    def install(self):
        pass
        

