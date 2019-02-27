# Standard library imports...
from __future__ import absolute_import
import json
import sys
import os
import urllib.request
from io import BytesIO
from unittest.mock import Mock, patch
import json
from pprint import pprint

# Third-party imports...
import pytest
import requests
import requests_mock

#sys.path.append("./Modules")
#sys.path.append("./base_switch")
#sys.path.append("./nxos")

#sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../base_switch')))
#sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../nxos')))
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../Switch')))

# from base_switch import Switch
import base_switch as switch
import nxos as nexus


# def setup_function(function):
#    '''setup des instances de la class Nxos pour les tests
#    iSpine1
#    iSpine2
#    '''
#    iSpine1 = nxos.Nxos('Spine1', 'user', 'passwd', port=443)
#    iSpine2 = nxos.Nxos('Spine2', 'user', 'passwd', port=443)

# def test_hostname():
#    iSpine1 = nxos.Nxos('Spine1', 'user', 'passwd', port=443)
#    print('iSpine1.hostname = {}'.format(iSpine1.host))
#    assert iSpine1.host == 'Spine1'

json_resp = {"id": 1, "jsonrpc": '2.0', "result": {"body": {"TABLE_interface": {"ROW_interface": [{"interface": 'mgmt0'},
                                                                                          {"desc": 'PINETA MGMT ',
                                                                                           "interface": 'Ethernet1/1',
                                                                                           "speed": '10G',
                                                                                           "type": 'eth'},
                                                                                          {'desc': 'BLT20 OA1',
                                                                                           'interface': 'Ethernet1/2',
                                                                                           'speed': '10G',
                                                                                           'type': 'eth'},
                                                                                          {'desc': 'BLT22 OA1',
                                                                                           'interface': 'Ethernet1/3',
                                                                                           'speed': '10G',
                                                                                           'type': 'eth'},
                                                                                          {'desc': 'CAULONIA MGMT ',
                                                                                           'interface': 'Ethernet1/4',
                                                                                           'speed': '10G',
                                                                                           'type': 'eth'},
                                                                                          {'desc': 'CAULONIA NIC1 ',
                                                                                           'interface': 'Ethernet1/5',
                                                                                           'speed': '10G',
                                                                                           'type': 'eth'},
                                                                                          {'desc': 'PROXMOXT1 MGMT ',
                                                                                           'interface': 'Ethernet1/6',
                                                                                           'speed': '10G',
                                                                                           'type': 'eth'},
                                                                                          {'desc': 'PROXMOXT1 NIC1 ',
                                                                                           'interface': 'Ethernet1/7',
                                                                                           'speed': '10G',
                                                                                           'type': 'eth'},
                                                                                          {'desc': 'PROXMOXT1 NIC3 ',
                                                                                           'interface': 'Ethernet1/8',
                                                                                           'speed': '10G',
                                                                                           'type': 'eth'},
                                                                                          {'desc': 'PROXMOXT1 Q1NIC1 ',
                                                                                           'interface': 'Ethernet1/9',
                                                                                           'speed': '10G',
                                                                                           'type': 'eth'},
                                                                                          {'desc': 'GLUSTERT21 nic0',
                                                                                           'interface': 'Ethernet1/10',
                                                                                           'speed': '10G',
                                                                                           'type': 'eth'},
                                                                                          {'desc': 'GLUSTERT21 mgmt',
                                                                                           'interface': 'Ethernet1/11',
                                                                                           'speed': '10G',
                                                                                           'type': 'eth'},
                                                                                          {'interface': 'Ethernet1/12',
                                                                                           'speed': '10G',
                                                                                           'type': 'eth'},
                                                                                          {'desc': 'GLUSTERT22 nic0',
                                                                                           'interface': 'Ethernet1/13',
                                                                                           'speed': '10G',
                                                                                           'type': 'eth'},
                                                                                          {'desc': 'GLUSTERT23 nic0',
                                                                                           'interface': 'Ethernet1/14',
                                                                                           'speed': '10G',
                                                                                           'type': 'eth'}, ]}}}}


class TestNxos:
    def setup_method(self):
        self.iSpine1 = nexus.Nxos('Spine1', 'user', 'passwd', port=443)
        self.iSpine2 = nexus.Nxos('Spine2', 'user', 'passwd', port=443)

    def test_get_host(self):
        assert self.iSpine1.host == 'Spine1'

    def test_set_host(self):
        self.iSpine1.host = 'testiSpine1'
        assert self.iSpine1.host == 'testiSpine1'

    def test_get_user(self):
        assert self.iSpine1.user == "user"

    def test_set_user(self):
        self.iSpine1.user = "test_user"
        assert self.iSpine1.user == 'test_user'

    def test_get_password(self):
        assert self.iSpine1.pwd == "passwd"

    def test_set_password(self):
        self.iSpine1.pwd = "test_password"
        assert self.iSpine1.pwd == "test_password"

    def test_get_port(self):
        assert self.iSpine1.port == 443

    def test_set_port(self):
        self.iSpine1.port = 80
        assert self.iSpine1.port == 80

    def test_set_nexus(self):
        iNexus = nexus.Nxos('test_nexus', 'test_user', 'test_pwd', 80)
        assert iNexus.host == 'test_nexus'
        assert iNexus.user == 'test_user'
        assert iNexus.pwd == 'test_pwd'
        assert iNexus.port == 80


#    def text_callback(self, request, context):
#        context.status_code = 200
#        context.headers['Test1'] = 'value1'
#        return results
#
#    def test_executeAPIcommand(self, requests_mock):
#
#        url = "http://{h}:{p}/{uri}".format(h=self.iSpine1.host,
#                                            p=self.iSpine1.port, uri='ins')
#        my_headers = {'content_type': 'application/json-rpc'}
#        my_payload = [{"jsonrpc": 2.0,
#                       "method": "cli",
#                       "params": {"cmd": "show interface description", "version": 1},
#                       "id": 1}
#                    ]
#
#        requests_mock.post(url, text=self.text_callback)
#        assert self.iSpine1.executeAPIcommand(my_headers, my_payload) == results

class TestexecuteiAPIcommand(object):
    my_headers = {'content_type': 'application/json-rpc'}
    my_payload = [{"jsonrpc": 2.0,
                   "method": "cli",
                   "params": {"cmd": "show interface description", "version": 1},
                   "id": 1}
                  ]

    @classmethod
    def setup_class(cls):
        cls.mock_post_patcher = patch('nxos.requests.post')
        cls.mock_post = cls.mock_post_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_post_patcher.stop()

    def test_execute_api_command_when_response_is_ok(self):
        # self.mock_post.return_value.ok = True
        self.mock_post.return_value = Mock(ok=True)
        self.mock_post.return_value.status_code = 200
        rep = json.dumps(json_resp, separators=(',',':'))
        self.mock_post.return_value.json = json.loads(rep)

        iNxos = nexus.Nxos('SPINE1', 'user', 'pwd', 80)

        my_headers = {'content_type': 'application/json'}
        my_payload = [{"jsonrpc": 2.0,
                       "method": "cli",
                       "params": {"cmd": "show interface description", "version": 1},
                       "id": 1}
                      ]
        #print('json_resp = ' + str(json_resp) + '\n')
        #print('type(json_resp) = ' + str(type(json_resp)) + '\n')
        #print('type(json.dumps(json_resp, separators=(\',\',\':\'))) = ' + str(type(json.dumps(json_resp, separators=(',',':')))) + '\n')
        resp = iNxos.execute_api_command(my_headers, my_payload)
        #print('\nresp = ')
        #pprint(resp)
        assert resp == json.loads(rep)['result']['body']

    def test_execute_api_command_when_response_is_not_ok(self):
        iNxos = nexus.Nxos('SPINE1', 'user', 'pwd', 80)
        my_headers = {'content_type': 'application/json-rpc'}
        my_payload = [{"jsonrpc": 2.0,
                       "method": "cli",
                       "params": {"cmd": "show interface description", "version": 1},
                       "id": 1}
                      ]

        # self.mock_post.return_value.ok = False
        self.mock_post.return_value = Mock(ok=False)
        self.mock_post.return_value.status_code = 500
        with pytest.raises(switch.NetworkCommandError):
            iNxos.execute_api_command(my_headers, my_payload)


class TestgetIntfAPI(object):
    @classmethod
    def setup_class(cls):
        cls.mock_post_patcher = patch('nxos.requests.post')
        cls.mock_post = cls.mock_post_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_post_patcher.stop()

    def test_get_intf_api_when_response_is_ok(self):
        json_resp = {"id": 1, "jsonrpc": '2.0', "result": {"body": {"TABLE_interface": {"ROW_interface": [{"desc": 'PINETA MGMT ',
                                                                                           "interface": 'Ethernet1/1',
                                                                                           "speed": '10G',
                                                                                           "type": 'eth'}]}}}}
        self.mock_post.return_value.ok = True
        self.mock_post.return_value = Mock()
        self.mock_post.return_value.status_code = 200
        rep = json.dumps(json_resp, separators=(',',':'))
        self.mock_post.return_value.json = json.loads(rep)

        iNxos = nexus.Nxos('SPINE1', 'user', 'pwd', 80)

        resp = iNxos.get_intf_api()
        print('\nresp = ')
        pprint(resp)

        intf1 = switch.Interface('Ethernet1/1', 'PINETA MGMT ')
        liste_retour = [intf1]

        assert len(resp) == len(liste_retour)
        assert resp[0] == liste_retour[0]

    def test_get_intf_api_when_desc_is_null(self):
        json_resp = {"id": 1, "jsonrpc": '2.0', "result": {"body": {"TABLE_interface": {"ROW_interface": [{
                                                                                           "interface": 'Ethernet1/1',
                                                                                           "speed": '10G',
                                                                                           "type": 'eth'}]}}}}
        self.mock_post.return_value = Mock(ok=True)
        self.mock_post.return_value.status_code = 200
        rep = json.dumps(json_resp, separators=(',', ':'))
        self.mock_post.return_value.json = json.loads(rep)

        iNxos = nexus.Nxos('SPINE1', 'user', 'pwd', 80)

        resp = iNxos.get_intf_api()
        print('\nresp = ')
        pprint(resp)

        intf1 = switch.Interface('Ethernet1/1','vide')
        liste_retour = [intf1]

        assert len(resp) == len(liste_retour)
        assert resp[0] == liste_retour[0]

    def test_get_intf_api_when_response_is_not_ok(self):
        iNxos = nexus.Nxos('SPINE1', 'user', 'pwd', 80)

        # self.mock_post.return_value.ok = False
        self.mock_post.return_value = Mock(ok=False)
        self.mock_post.return_value.status_code = 500
        with pytest.raises(switch.NetworkCommandError):
            iNxos.get_intf_api()
