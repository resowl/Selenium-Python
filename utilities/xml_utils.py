import requests
from xml.etree import ElementTree as et
from utilities import path_utils


class XML_Class_Page:

    def check_root_of_xml_response(self, url):
        response = requests.get(url)
        response_body_as_xml = et.fromstring(response.content)
        xml_tree = et.ElementTree(response_body_as_xml)
        root = xml_tree.getroot()
        print(root.tag, len(root.attrib), root.text)

    def check_specific_element_of_xml_response(self, url, key_to_find, value_to_be ):
        response = requests.get(url)
        response_body_as_xml = et.fromstring(response.content)
        xml_tree = et.ElementTree(response_body_as_xml)
        key_value = xml_tree.find(key_to_find)
        assert key_value.text == value_to_be

    def find_in_xml_file(self, xml_file):
        tree = et.parse(xml_file) # create element tree object
        root = tree.getroot()  # get root element
        print(root.tag)
        print(root.attrib)
        for child in root:
            print("childtag is-->",child.tag,"child attributeis--->", child.attrib)
            if child.tag == 'book':
                print(child.get('id'))
                for attributes in child:
                    # if (attributes.tag=='author'or attributes.tag=='title' or attributes.tag=='genre'):
                        print(attributes.text)


    def find_in_xml_string(self, xml_string):
        root= et.fromstring(xml_string)
        print(root.tag)
        print(root.attrib)
        for child in root:
            print("child tag is-->", child.tag, "child attribute is--->", child.attrib)
        for child in root.findall("book"):
            author = child.find("author").text #can be changed to whatever we need to find
            title = child.find("title").text
            print(author, title)




c= XML_Class_Page()
print("@@@@@@@@@@@@@")
c.find_in_xml_file(path_utils.get_file("sample.xml"))




