# Build-in imports
from __future__ import absolute_import
import sys
import os

import xml.etree.ElementTree as et
import pytest

#sys.path.append("./Modules")
#sys.path.append('./base_switch')
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '../Switch')))

# from base_switch import Switch
import base_switch as switch

class TestInterface(object):
    def setup_method(self):
        self.iIntf1 = switch.Interface('eth1/1', 'BLT01 VC1X1')
        self.iIntf2 = switch.Interface('eth1/2', 'BLT01 VC2X1')
        self.iIntf3 = switch.Interface('eth1/52', 'VPC-PEER')
        self.iIntf4 = switch.Interface('eth1/53', 'VPC-PEER')

    def test_get_interface(self):
        assert self.iIntf1.name == 'eth1/1'
        assert self.iIntf1.description == 'BLT01 VC1X1'

    def test_set_intf_name(self):
        self.iIntf1.name = 'eth1/3'
        assert self.iIntf1.name == 'eth1/3'

    def test_set_intf_desc(self):
        self.iIntf1.description = 'testIntf'
        assert self.iIntf1.description == 'testIntf'


class TestSwitch(object):
    def setup_method(self):
        self.iSwitch = switch.Switch("Spine1", "user1", "pwd1", 830)

    #	@pytest.fixture(scope="class")
    #	def list_intf():
    #		self.iIntf1 = switch.Interface('eth1/1', 'BLT01 VC1X1')
    #		self.iIntf2 = switch.Interface('eth1/2', 'BLT01 VC2X1')
    #		self.iIntf3 = switch.Interface('eth1/52', 'VPC-PEER')
    #		self.iIntf4 = switch.Interface('eth1/53', 'VPC-PEER')
    #		self.iSwitch.intf = [self.iIntf1, self.iIntf2, self.iIntf3, self.iIntf4]
    #		print(self.iSwitch.intf)
    #		return self.iSwitch.intf

    def test_get_switch(self):
        assert self.iSwitch.host == "Spine1"
        assert self.iSwitch.user == "user1"
        assert self.iSwitch.pwd == "pwd1"
        assert self.iSwitch.port == 830

    def test_set_switch_host(self):
        self.iSwitch.host = "Spine2"
        assert self.iSwitch.host == "Spine2"

    def test_set_switch_user(self):
        self.iSwitch.user = "user2"
        assert self.iSwitch.user == 'user2'

    def test_set_switch_pwd(self):
        self.iSwitch.pwd = 'pwd2'
        assert self.iSwitch.pwd == 'pwd2'

    def test_set_switch_port(self):
        self.iSwitch.port = 80
        assert self.iSwitch.port == 80

    def test_set_switch_intf(self):
        self.iIntf1 = switch.Interface('eth1/1', 'BLT01 VC1X1')
        self.iIntf2 = switch.Interface('eth1/2', 'BLT01 VC2X1')
        self.iIntf3 = switch.Interface('eth1/52', 'VPC-PEER')
        self.iIntf4 = switch.Interface('eth1/53', 'VPC-PEER')
        self.iSwitch.intf = [self.iIntf1, self.iIntf2,
                             self.iIntf3, self.iIntf4]
        # self.iSwitch.intf = list_intf
        assert self.iSwitch.intf == [self.iIntf1, self.iIntf2,
                                     self.iIntf3, self.iIntf4]

    def test_search_intf1(self):
        self.iIntf1 = switch.Interface('eth1/1', 'BLT01 VC1X1')
        self.iIntf2 = switch.Interface('eth1/2', 'BLT01 VC2X1')
        self.iIntf3 = switch.Interface('eth1/52', 'VPC-PEER')
        self.iIntf4 = switch.Interface('eth1/53', 'VPC-PEER')
        self.iSwitch.intf = [self.iIntf1, self.iIntf2,
                             self.iIntf3, self.iIntf4]
        assert self.iSwitch.search_intf('BLT') == [self.iIntf1, self.iIntf2]

    def test_search_intf2(self):
        self.iIntf1 = switch.Interface('eth1/1', 'BLT01 VC1X1')
        self.iIntf2 = switch.Interface('eth1/2', 'BLT01 VC2X1')
        self.iIntf3 = switch.Interface('eth1/52', 'VPC-PEER')
        self.iIntf4 = switch.Interface('eth1/53', 'VPC-PEER')
        self.iSwitch.intf = [self.iIntf1, self.iIntf2,
                             self.iIntf3, self.iIntf4]
        assert self.iSwitch.search_intf('') == [self.iIntf1, self.iIntf2, self.iIntf3, self.iIntf4]

