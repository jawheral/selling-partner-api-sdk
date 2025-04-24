# coding: utf-8

from __future__ import absolute_import

import unittest
import requests
import random

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.catalogitems_v2022_04_01.catalog_api import CatalogApi

import spapi.models.catalogitems_v2022_04_01 as models

class TestCatalogApi(unittest.TestCase):
    """CatalogApi unit test stubs"""

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
        self.api = CatalogApi(client.api_client)

    def tearDown(self):
        pass

    def test_get_catalog_item(self):
        asin = random.random()
        marketplace_ids = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_catalog_item"), "200")
        response = self.api.get_catalog_item_with_http_info(asin, marketplace_ids, included_data=None, locale=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_search_catalog_items(self):
        marketplace_ids = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("search_catalog_items"), "200")
        response = self.api.search_catalog_items_with_http_info(marketplace_ids, identifiers=None, identifiers_type=None, included_data=None, locale=None, seller_id=None, keywords=None, brand_names=None, classification_ids=None, page_size=None, page_token=None, keywords_locale=None)
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