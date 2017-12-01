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
        Consider using the 'renderer_context' argument to set the 'publisher' and 'publisherurl' elements.
        """
        print(dir(renderer_context['request']))
        print(' ')
        print(renderer_context['request'].data)
        # Helper variables
        root_tag_name = 'source'
        item_tag_name = 'job'
        # Build the root xml element:
        root = E.Element(root_tag_name)
        # Add the 'publisher' element:
        E.SubElement(root, 'publisher').text = 'ATS NAME'
        # Add the 'publisherurl' element:
        E.SubElement(root, 'publisherurl').text = 'http://www.atssite.com'
        # Unpack each dictionary from the data list:
        for d in data:
            # Create a job tag:
            job = E.SubElement(root, item_tag_name)
            # Loop through each ordered dictionary:
            for key, value in d.items():
                # Add each key, value pair to an element and assign to job tag:
                E.SubElement(job, key).text = '<![CDATA[' + value + ']]>'

                
        # print(E.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))
        # Pass the completed XML document to the view:
        return E.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8')
