import json
from configuration.config import TestData
from utilities.json_utils import Jsondata_Class_Page
import requests
     #practice work
class Test_Req_Res():
    auth_token = "3b431062780351dd03b6c7a3a773a4a22645ef1c33eab67ec920ec3056e0ef45"
    header = {'Content_Type': 'application/json'}
    # 'Accept': 'application/json','Authorization': 'Bearer' + auth_token}


    def test_read_response(self):
        j=Jsondata_Class_Page()
        response = j.get(TestData.URL)
        # print("response------------>", response.text)
        # assert j.check_status_code(response,200)
        # assert j.check_header_as_per_requirement(response, 'content_type', 'application/json')
        # header = j.get_header(TestData.URL)
        # print("Header is----------->", header)
        # dict = json.loads(response.text)
        # print("Dict is-------------->", dict)
        # for keyval in dict:
        #     # print("The value of", keyval, "is-->", keyval['name'])
        #     print("All email's are---->", keyval['email'])
        dict = j.conver_json_string_to_python_dictionary(response.text)
        for keyval in dict:
            # print("The value of", keyval, "is-->", keyval['name'])
            # print("All email's are---->", keyval['email'])
            if keyval['name'] =='Clementina DuBuque':
                print("Email is------------>", keyval['email'])
                print("Keyval is---------------->", keyval)


#     def test_update_resp(self):
#         response = self.get(TestData.URL)
#         value = self.check_status_code(response, 200)
#         assert value
#
    # def test_element_present(self):
    #     response = self.test_read_response()
    #     value = self.check_element_in_a_dictionary(response, "name", "Kartik Marar")
    #     assert value
#
#     def test_header(self):
#         response = self.get(TestData.URL)
#         value = self.check_header_as_per_requirement(response, "Content-Type", "application/json")
#         assert value
#
#     def test_status_resp(self):
#         response = self.get(TestData.URL)
#         value = response.raise_for_status()
#         print(value)
#
#     def test_header_text(self, response):
#         response = self.get(TestData.URL)
#
#         header = self.get_header(response)
#         print(header)
#
# ########################################



