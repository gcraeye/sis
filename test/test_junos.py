from __future__ import absolute_import
import sys
import os

# third-party import
import urllib.request
from io import BytesIO
import json

#sys.path.append("./Modules")
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../Switch')))
#sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../Switch/junos')))

# local import
import base_switch as switch
import junos as juniper

class TestJunos:
    def setup_method(self):
        self.iSpine1 = juniper.Junos('Spine1', 'user', 'passwd', port=443)
        self.iSpine2 = juniper.Junos('Spine2', 'user', 'passwd', port=443)

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
        inexus = juniper.Junos('test_nexus', 'test_user', 'test_pwd', 80)
        assert inexus.host == 'test_nexus'
        assert inexus.user == 'test_user'
        assert inexus.pwd == 'test_pwd'
        assert inexus.port == 80

    def test_http_return(self, monkeypatch):
        results = [
        ]

        def mockreturn(request):
            return BytesIO(json.dumps(results).encode())

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        assert self.iSpine1.connect() == results
