import pytest
import requests
import csv
import xml.etree.ElementTree as et
import responses
from pprint import pprint
import json
import jsonpath
from lxml import etree
from cerberus import Validator
from assertpy.assertpy import assert_that, soft_assertions

class BasePg:
    auth_token = "3b431062780351dd03b6c7a3a773a4a22645ef1c33eab67ec920ec3056e0ef45"
    headers = {'Content_Type': 'application/json'}
        # headers = {'Content_Type': 'application/json', 'Accept': 'application/json',
        #                 'Authorization': 'Bearer' + auth_token}

    def get(self, url):
        response = requests.get(url)
        return response

    def post(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        return response

    def delete(self, url):
        response = requests.delete(url)
        return response

    def put(self, url, json_format_input_data, success_code):
        response = requests.put(url, json_format_input_data)
        self.check_resp_code(response, success_code)

    def get_value_after_update(self, response, value_of):
        response_json = json.loads(response.text)
        updated_list = jsonpath.jsonpath(response_json, value_of)
        return (updated_list[0])

    def check_resp_code(self, response, code):
        return response.status_code == code

    def check_header(self, response, type, format):
        return response.headers[type] == format

    def check_element_in_a_dictionary(self, response, key, value):
        response_python_dict = response.json()
        all_entries_list = [entry[key]for entry in response_python_dict]
        return value in all_entries_list

    def read_data_from_csv(self, file_name):
        test_data_from_csv = []
        with open(file_name) as file:
            data = csv.reader(file)
            for row in data:
                test_data_from_csv.append(row)
            return test_data_from_csv

    def check_specific_element_of_xml_response(self, response, find_element, element_value):
        response_body_as_xml = et.fromstring(response.content)
        xml_tree = et.ElementTree(response_body_as_xml)
        element = xml_tree.find(find_element)
        return element.text == element_value

    def add_responses_in_error_message(self, url, error_message):
        responses.add(responses.GET, url, body=ValueError(error_message))
        with pytest.raises(ValueError) as ve:
            self.get(url)
        return str(ve.value) == error_message

    def pretty_print(msg, indent=int(2)):
        pprint(msg, indent=indent)

    def add_new_data_from_file(self, url, file_path):
        f = open(file_path, 'r')
        request_json = json.loads(f.read())
        response = requests.post(url, request_json)
        return response.text

    def fetch_data_from_response_after_post(self, response, fetch_value_of):
        value = jsonpath.jsonpath(response.json(), fetch_value_of)
        return value[0]

    def validate_schema(self, response, schema):
        all_entries = json.loads(response.text) #we will get list of dictionaries
        # print(all_entries)
        v = Validator(schema, require_all=True)
        with soft_assertions():
           for entry in all_entries:
               is_valid = v.validate(entry)
               return is_valid
               # assert_that(is_valid, description=v.errors).is_true()















