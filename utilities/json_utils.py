import json
import jsonpath
import requests
import csv
from cerberus import Validator
from assertpy.assertpy import assert_that, soft_assertions
from pprint import pprint
import responses
import pytest
import jsonschema
from jsonschema import validate
from requests.exceptions import HTTPError

class Jsondata_Class_Page:

    def get(self, url):
        retries = 3
        for n in range(retries):
            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.exceptions.ConnectionError as err:
                # eg, no internet
                raise SystemExit(err)
            except requests.exceptions.HTTPError as err:
                # eg, url, server and other errors
                raise SystemExit(err)
            return response

    # The dumps() function of the json module dumps a dictionary into JSON contents, and returns a JSON string.
    def convert_python_dict_to_json_string(self, python_dict):
        json_string = json.dumps(python_dict,sort_keys=True, ensure_ascii=False, indent=4),
        return json_string

    def store_json_string_to_a_file(self,file_name, json_string):
        with open(file_name, 'w') as f:
            f.write(json_string)

    def conver_json_string_to_python_dictionary(self, json_string):
        python_dictionary = json.loads(json_string)
        return(python_dictionary)

    def check_status_code(self, response, code):
        return response.status_code == code

    def put(self, url, json_format_input_data, success_code):
        response = requests.put(url, json_format_input_data)
        value = self.check_status_code(response, success_code)
        return value

    def check_header_as_per_requirement(self, response, type, format):
        return response.headers[type] == format

    def delete(self, url):
        response = requests.delete(url)
        return response

    def get_header(self, url):
        x = requests.head(url)
        # print the response headers (the HTTP headers of the requested file):
        return (x.headers)

    def reading_json_data_from_a_file(self, json_data):
        with open(json_data, "r") as json_file:
            data = json.load(json_file) #json.loads(): To parse JSON from String.json.load() to Parse JSON from a file.
            return(data)

    def get_response_and_check_status_code(self, url):
        response = requests.get(url)
        return response.status_code

    def get_response_and_check_content_type_is_application_json(self, url):
        response = requests.get("http://api.zippopotam.us/us/90210")
        return response.headers["Content-Type"] == "application/json"

    def get_response_and_check_if_key_equals_value(self, url, key, value):
        response = requests.get(url)
        response_body = response.json()
        return response_body[key] == value

    def read_data_from_csv(self, csv_file):
        test_data_from_csv = []
        with open(csv_file, newline="") as csvfile:
            data = csv.reader(csvfile, delimiter=",")
            for row in data:
                test_data_from_csv.append(row)
        return test_data_from_csv

    def download_an_image(self, url, filename):
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
            print(f'{filename} is downloaded')

    def iterate_through_python_dictionary(self, python_dict):
        print("Print each key-value pair from JSON response")
        for key, value in python_dict.items():
            print(key, ":", value)
            return(key, ":", value)

    def post_json_data(self, url, json_data):
        response = requests.post(url, data=json_data, headers={'Content_Type': 'application/json'})
        return response

    def post_xml_data(self, url, xml_data):
        response = requests.post(url, headers={"Content-Type": "application/xml"}, data=xml_data)
        return response.headers["Content-Type"] == "application/xml", response.status_code == 200

    def pretty_print(msg, indent=2):
        pprint(msg, indent=indent)

    def validate_schema(self, response, schema):
        all_entries = json.loads(response.text)  # we will get list of dictionaries
        # print(all_entries)
        v = Validator(schema, require_all=True)
        with soft_assertions():
            for entry in all_entries:
                is_valid = v.validate(entry)
                return is_valid
        # assert_that(is_valid, description=v.errors).is_true()

    def validate_json_data_string_is_valid_or_not(self, json_data_string):
        try:
            json.loads(json_data_string)
        except ValueError as err:
            return False
        return True

    def validate_json_and_respective_schema(self, jsonData, schema_string): #pass json data after converting into python object using loads()
        try:
            validate(instance=jsonData, schema=schema_string)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True

    def add_responses_in_error_message(self, url, error_message):
        responses.add(responses.GET, url, body=ValueError(error_message))
        with pytest.raises(ValueError) as ve:
            self.get(url)
        return str(ve.value) == error_message

    def get_all_values_of_a_dictionary(self, response, key, value):
        response_python_dict = response.json()
        all_entries_list = [entry[key] for entry in response_python_dict]
        return value in all_entries_list

    def add_new_data_from_file(self, url, file_path):
        f = open(file_path, 'r')
        request_json = json.loads(f.read())
        response = requests.post(url, request_json)
        return response.text

    def fetch_data_from_response_after_post(self, response, fetch_value_of):
        value = jsonpath.jsonpath(response.json(), fetch_value_of)
        return value[0]

    def check_element_in_a_dictionary(self, response, key, value):
        response_python_dict = response.json()
        all_entries_list = [entry[key]for entry in response_python_dict]
        return value in all_entries_list

    def get_value_after_update(self, response, value_of):
        response_json = json.loads(response.text)
        updated_list = jsonpath.jsonpath(response_json, value_of)
        return (updated_list[0])




