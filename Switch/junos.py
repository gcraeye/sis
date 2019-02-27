#!/usr/bin/env python
""" Class junos :
Permet de gerer les switchs junos

"""
from __future__ import absolute_import
import sys
import os
from pprint import pformat

from jnpr.junos import Device
from jnpr.junos.exception import *

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), './')))

# from . import switch
#import base_switch as switch
from base_switch import *

class Junos(Switch):
    """ Definition de la classe junos
    parametres de la classe
    - host : IP de l'equipement
    - username
    - pasword
    - port

    fonctions de la classe:
    - connect
    """

    def __init__(self, host, user, pwd, port=830):
        """ Definition de la classe
        parametres: host, user, pwd, port
        """
        #switch.Switch.__init__(self, host, user, pwd, port)
        super().__init__(host, user, pwd, port)
        self.os = "junos"

    def connect(self):
        """ Connection au switch """
        try:
            with Device(host=self.host, user=self.user, password=self.pwd, port=self.port).open as dev:
                return dev
        except ConnectRefusedError:
            print("%s: Error - Device connection refused!" % self.host)
        except ConnectTimeoutError:
            print("%s: Error - Device connection timed out!" % self.host)
        except ConnectAuthError:
            print("%s: Error - Authentication failure!" % self.host)
        except ConnectUnknownHostError:
            print("%s: Error - Connection attempt to unknown host." % self.host)
        except ConnectionError:
            print("%s: Connection error!" % self.host)

    def __del__(self):
        """ Avant de supprimer la classe, on ferme la connection
        """
        self.dev.close

    def __repr__(self):
        """ Affiche les informations du switch
        """
        pformat(self.facts)

    def show_intf(self):
        """ Retourne la liste des interfaces au format json
        """
        dev = self.connect()
        res = dev.rpc.get_interface_information({"format": "json"}, terse=True).json
        return res
