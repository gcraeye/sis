#!/usr/bin/env python
""" Class switch :
manage switch

"""

from Switch import Interface
from Switch import SwitchError

        
class SwitchError(BaseException):
    pass


class NetworkCommandError(SwitchError):
    pass


# class Interface(object):
#     """Define an interface for switch interfaces
# 
#     parameters
#     name (str)
#     description (str)
# 
#     """
# 
#     def __init__(self, name, desc):
#         """Constructor for Interface class
# 
#         parameters
#         name (str)
#         description (str)
# 
#         """
#         self.name = name
#         self.description = desc
# 
#     def __eq__(self, other):
#         return ( self.name == other.name and self.description == other.description )
# 
#     def serialize(self, serializer):
#         serializer.start_object('name', self.name)
#         serializer.add_property('description', self.description)


class Switch(object):
    """Manage switch via netconf
    parameters :
    - host : IP address or hostname
    - username
    - password
    - port

    Method:
    - connect
    - search_intf
    """

    def __init__(self, host, user, pwd, port):
        """ Definition de la classe
        parametres: host, user, pwd, port
        """
        self.host = host
        self.user = user
        self.pwd = pwd
        self.port = port
        self.intf = []

    #    @abstractmethod
    #    def connect(self):
    #        """Permet de connecter sur le port netconf du switch
    #        et verifie que le switch a bien la capability openconfig
    #        """
    #        pass
    #
    #    @abstractmethod
    #    def show_intf(self):
    #        pass

    def search_intf(self, chaine):
        """Fonction qui recherche les interfaces contenant la chaine de recherche
        =========================================================================
        Parametres :
            chaine : chaine de caracteres a rechercher

        Retourne :
            res : objet json
        """
        chaine = chaine.upper()
        rep = []
        for interface in self.intf:
            try:
                if interface.description.find(chaine) != -1:
                    rep.append(interface)
            except KeyError:
                continue
        return rep
