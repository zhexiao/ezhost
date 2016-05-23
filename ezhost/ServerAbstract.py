# -*- coding: utf-8 -*-
"""
Abstract class for all server class
"""

# internal libs
from abc import ABCMeta, abstractmethod

class ServerAbstract(metaclass=ABCMeta):
    @abstractmethod
    def install(self):
        pass
        

