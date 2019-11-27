
class Interface(object):
    """Define an interface for switch interfaces
    parameters
    name (str)
    description (str)
    """

    def __init__(self, name, desc):
        """Constructor for Interface class
        parameters
        name (str)
        description (str)
        """
        self.name = name
        self.description = desc

    def __eq__(self, other):
        return ( self.name == other.name and self.description == other.description )

    def serialize(self, serializer):
        serializer.start_object('name', self.name)
        serializer.add_property('description', self.description)

