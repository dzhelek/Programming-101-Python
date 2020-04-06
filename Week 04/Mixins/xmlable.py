import xml.etree.ElementTree as ET


class Xmlable:
    def to_xml(self):
        name = ET.Element(type(self).__name__)
        for attribute in self.__dict__:
            attr = ET.SubElement(name, attribute, text = self.__dict__[attribute])
            # value = ET.SubElement(attr, self.__dict__[attribute])
        return ET.dump(name)

    @classmethod
    def from_xml(cls, xml_string):
        return cls(xml_string)
