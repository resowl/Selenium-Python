import json

from api_testing.pages.basepage import BasePg
from configuration.config import TestData

     #practice work
class Test_Req_Res(BasePg):
    auth_token = "3b431062780351dd03b6c7a3a773a4a22645ef1c33eab67ec920ec3056e0ef45"
    header = {'Content_Type': 'application/json'}
    # 'Accept': 'application/json','Authorization': 'Bearer' + auth_token}

    def test_read_response(self):
        response = self.get(TestData.URL)
        print(response.json())


    def test_update_resp(self):
        response = self.get(TestData.URL)
        value = self.check_resp_code(response, 200)
        assert value

    def test_element_present(self):
        response = self.get(TestData.URL)
        value = self.check_element_in_a_dictionary(response, "name", "Kartik Marar")
        assert value

    def test_header(self):
        response = self.get(TestData.URL)
        value = self.check_header(response, "Content-Type", "application/json")
        assert value


