"""
Provides XML rendering support.
"""

from rest_framework.renderers import BaseRenderer
import lxml.etree as E


class XMLRenderer(BaseRenderer):
    """
    Renderer which serializes to XML.
    """

    media_type = 'application/xml'
    format = 'xml'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized XML.
        """
        # Helper variables
        root_tag_name = 'source'
        item_tag_name = 'job'
        utf8_parser = E.XMLParser(encoding='utf-8')
        # Start building xml:
        root = E.Element(root_tag_name)
        # Unpack each dictionary from the data list:
        for d in data:
            # Create a job tag:
            job = E.SubElement(root, item_tag_name)
            # Loop through each ordered dictionary:
            for key, value in d.items():
                # Add each key, value pair to an element and assign to job tag:
                E.SubElement(job, key).text = value

                
        print(E.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))
        # Pass the completed XML document to the view:
        return E.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8')
