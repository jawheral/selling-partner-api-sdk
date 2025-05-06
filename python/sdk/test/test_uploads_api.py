# coding: utf-8

from __future__ import absolute_import

import requests
import rstr

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.uploads_v2020_11_01.uploads_api import UploadsApi

import spapi.models.uploads_v2020_11_01 as models

class TestUploadsApi(unittest.TestCase):
    """UploadsApi unit test stubs"""

    def setUp(self):
        # Tests Mock Server
        self.mock_server_endpoint = "http://localhost:3000"
        self.mock_server_endpoint_oauth = "http://localhost:3000/auth/o2/token"
        config = SPAPIConfig(
            client_id="clientId",
            client_secret="clientSecret",
            refresh_token="refreshToken",
            region="NA",
            scope = None
        )
        client = SPAPIClient(config, self.mock_server_endpoint_oauth, self.mock_server_endpoint)
        self.api = UploadsApi(client.api_client)

    def tearDown(self):
        pass

    def test_create_upload_destination_for_resource(self):
        marketplace_ids = [self._get_random_value("List[str]") for _ in range(1)]
        content_md5 = self._get_random_value("str", None)
        resource = self._get_random_value("str", None)
        
        self.instruct_backend_mock(self.to_camel_case("create_upload_destination_for_resource"), "201")
        response = self.api.create_upload_destination_for_resource_with_http_info(marketplace_ids, content_md5, resource, )
        self.assertEqual(201, response[1])
        self.assert_valid_response_payload(201, response[0])
        pass


    def instruct_backend_mock(self, response: str, code: str) -> None:
        url = f"{self.mock_server_endpoint}/response/{response}/code/{code}"
        ## handle same api operation name exceptions
        if "vendor" in "api.uploads_v2020_11_01" and response == "getOrder":
            url += f"?qualifier=Vendor"
        if "fulfillment_inbound" in "api.uploads_v2020_11_01" and response == "getShipment":
            url += f"?qualifier=FbaInbound"
        requests.post(url)

    def _get_random_value(self, data_type, pattern=None):
        if pattern:
            return rstr.xeger(pattern)

        basic_types = {
            'str': "test_string",
            'string': "test_string",
            'int': 123,
            'integer': 123,
            'float': 123.45,
            'bool': True,
            'boolean': True
        }

        return basic_types.get(data_type.lower(), {})

    def assert_valid_response_payload(self, status_code: int, body: any) -> None:
        if status_code != 204:
            self.assertIsNotNone(body)

    def to_camel_case(self, snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    unittest.main()