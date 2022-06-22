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
        value = self.check_status_code(response, 200)
        assert value

    def test_element_present(self):
        response = self.get(TestData.URL)
        value = self.check_element_in_a_dictionary(response, "name", "Kartik Marar")
        assert value

    def test_header(self):
        response = self.get(TestData.URL)
        value = self.check_header_as_per_requirement(response, "Content-Type", "application/json")
        assert value

    def test_status_resp(self):
        response = self.get(TestData.URL)
        value = response.raise_for_status()
        print(value)

    def test_header_text(self, response):
        response = self.get(TestData.URL)

        header = self.get_header(response)
        print(header)

