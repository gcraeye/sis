#!/usr/bin/env python
""" Class nxos :
Permet de gerer les switchs nxos

"""
# Build-in import
from __future__ import absolute_import
import json
import sys
from pprint import pprint

# third-party import
import requests

#sys.path.append("./base_switch")
#sys.path.append("./nxos")

# local import
import base_switch as switch


# from . import Switch

# disable warnings from SSL/TLS certificates
# requests.packages.urllib3.disable_warnings()

class Nxos(switch.Switch):
    def __init__(self, hostname, username, password, port=443):
        # Switch.__init__(self, hostname, username, password, port)
        super().__init__(hostname, username, password, port)
        self.os = 'nxos'

    def connect(self):
        """Methode de connection au NXAPI des switchs NEXUS
         =================================================
         Retourne un cookie d'authentification
         """
        http_header = {}
        url = 'https://{h}/api/mo/aaaLogin.json'.format(h=self.host)
        http_header["HOST"] = self.host
        payload = "aaaUser name={user} pwd={pwd}".format(user=self.user, pwd=self.pwd)
        try:
            req = requests.post(url=url, data=payload, headers=http_header)
        except Exception as e:
            print('failed to obtain auth cookie : {e}'.format(e))
            sys.exit(1)
        else:
            cookie = req.headers['Set-Cookie']
            return cookie

    def generic_get_request(self, cookie, apiurl, verb, desc):
        """
	
	  """
        http_header = {}
        url = "https://{h}{apiurl}".format(h=self.host, apiurl=apiurl)
        http_header['Cookie'] = cookie
        http_header["Host"] = self.host
        try:
            req = requests.request(verb, url=url, headers=http_header)
        except:
            print("There is a problem with the {} request !".format(verb))
        else:
            return req

    def execute_api_command(self, headers, payload):
        url = 'http://{h}:{p}/ins'.format(h=self.host, p=self.port)
        payload = json.dumps(payload)
        auth = (self.user, self.pwd)
        resp = requests.post(url, data=payload, headers=headers, auth=auth)
        if resp.ok:
            tmp = resp.json
            #tmp = json.loads(tmp)
            #print('\ntmp[\'result\'][\'body\'] = \n')
            #pprint(tmp['result']['body'])
            return tmp['result']['body']
        else:
            raise switch.NetworkCommandError()

    def get_intf_api(self):
        my_headers = {'content_type': 'application/json-rpc'}
        my_payload = [{"jsonrpc": 2.0,
                       "method": "cli",
                       "params": {"cmd": "show interface description", "version": 1},
                       "id": 1}
                      ]
        result = self.execute_api_command(my_headers, my_payload)

        list_intf = result['TABLE_interface']['ROW_interface']
        liste_retour = []
        for intf in list_intf:
            if 'desc' not in intf:
                intf['desc'] = 'vide'
            print('\nintf = \n')
            pprint(intf)
            tmp = switch.Interface(name=intf['interface'], desc=intf['desc'])
            liste_retour.append(tmp)
        print('\nliste_retour = \n')
        pprint(liste_retour)
        return liste_retour
