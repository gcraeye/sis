# Build-in imports
from __future__ import absolute_import

import sys
import xml.etree.ElementTree as et

import pytest

sys.path.append("./Modules")
sys.path.append('./base_switch')
sys.path.append('./Serializer')

# from base_switch import Switch
import base_switch as switch
from base_switch import Interface
from Serializer import *


#from serializer import JsonSerializer as JsonSerializer
#from base_switch import XmlSerializer

class TestSerializer(object):
    @pytest.fixture()
    def iIntf1(self):
        self.iIntf1 = Interface('eth1/1', 'BLT01 VC1X1')

    def test_serialize_intf_json(self, iIntf1):
        factory = SerializerFactory()
        #factory.register_format('JSON', JsonSerializer)
        #factory.register_format('XML', XmlSerializer)
        #serializer = ObjectSerializer()
        Intf_JSON = JsonSerializer()
        Intf_JSON.start_object(iIntf1, 1)
        Intf_JSON.add_property('name', iIntf1.name)
        Intf_JSON.add_property('desc', iIntf1.description)
        test = serializer.serialize(iIntf1, "JSON")
        assert test == {"name": 'eth1/1', "desc": 'BLT01 VC1X1'}

    def test_serialize_intf_xml(self):
        intf_info = et.Element('interface', attrib={'name': 'eth1/1'})
        desc = et.SubElement(intf_info, 'desc')
        desc.text = 'BLT01 VC1X1'
        assert switch.Serializer(self.iIntf1, 'XML').tostring == intf_info.tostring