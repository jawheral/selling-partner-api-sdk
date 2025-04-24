# coding: utf-8

from __future__ import absolute_import

import unittest
import requests
import random

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.product_type_definitions_v2020_09_01.definitions_api import DefinitionsApi

import spapi.models.product_type_definitions_v2020_09_01 as models

class TestDefinitionsApi(unittest.TestCase):
    """DefinitionsApi unit test stubs"""

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
        self.api = DefinitionsApi(client.api_client)

    def tearDown(self):
        pass

    def test_get_definitions_product_type(self):
        product_type = random.random()
        marketplace_ids = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_definitions_product_type"), "200")
        response = self.api.get_definitions_product_type_with_http_info(product_type, marketplace_ids, seller_id=None, product_type_version=None, requirements=None, requirements_enforced=None, locale=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_search_definitions_product_types(self):
        marketplace_ids = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("search_definitions_product_types"), "200")
        response = self.api.search_definitions_product_types_with_http_info(marketplace_ids, keywords=None, item_name=None, locale=None, search_locale=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass


    def instruct_backend_mock(self, response: str, code: str) -> None:
        url = f"{self.mock_server_endpoint}/response/{response}/code/{code}"
        requests.post(url)

    def assert_valid_response_payload(self, status_code: int, body: any) -> None:
        if status_code != 204:
            self.assertIsNotNone(body)

    def to_camel_case(self, snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    unittest.main()