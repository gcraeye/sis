import json
import xml.etree.ElementTree as et


class SerializerFactory:
    #def __init__(self):
    #    self._creators = {}
    #
    #def register_format(self, format, creator):
    #    self._creators[format] = creator
    #
    #def get_serializer(self, format):
    #    creator = self._creators.get(format)
    #    if not creator:
    #        raise ValueError(format)
    #    return creator()

    def get_serializer(self, format):
        if format == 'JSON':
            return JsonSerializer()
        elif format == 'XML':
            return XmlSerializer()
        else:
            raise ValueError(format)


class ObjectSerializer:
    def serialize(self, serializable, out):
        serializer = SerializerFactory.get_serializer(out)
        serializable.serialize(serializer)
        return serializer.to_str()


class JsonSerializer(object):
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer(object):
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.ElementTree(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')