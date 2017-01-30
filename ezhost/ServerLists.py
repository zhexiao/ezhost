from enum import Enum

"""
All valid server lists
"""


class ServerLists(Enum):
    ServerLamp = 'lamp'
    ServerLnmp = 'lnmp'
    ServerDjango = 'django'
    ServerDjangoUwsgi = 'django-uwsgi'
    ServerLnmpWordpress = 'lnmp-wordpress'
