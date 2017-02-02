from enum import Enum


class ServerLists(Enum):
    """
        All valid server lists and shortcut
    """

    ServerLamp = 'lamp'
    ServerLnmp = 'lnmp'
    ServerDjango = 'django'
    ServerDjangoUwsgi = 'django-uwsgi'
    ServerLnmpWordpress = 'lnmp-wordpress'
