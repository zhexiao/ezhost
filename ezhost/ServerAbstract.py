# -*- coding: utf-8 -*-
"""
Abstract class for all server class
"""

# internal libs
import os
from abc import ABCMeta, abstractmethod, abstractproperty

class ServerAbstract(metaclass=ABCMeta):
    @property
    def command_path(self):
        return os.path.dirname(os.path.realpath(__file__))

    @abstractmethod
    def install(self):
        pass
        

