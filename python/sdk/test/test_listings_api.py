# coding: utf-8

from __future__ import absolute_import

import unittest
import requests
import random

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.listings_items_v2021_08_01.listings_api import ListingsApi

import spapi.models.listings_items_v2021_08_01 as models

class TestListingsApi(unittest.TestCase):
    """ListingsApi unit test stubs"""

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
        self.api = ListingsApi(client.api_client)

    def tearDown(self):
        pass

    def test_delete_listings_item(self):
        seller_id = random.random()
        sku = random.random()
        marketplace_ids = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("delete_listings_item"), "200")
        response = self.api.delete_listings_item_with_http_info(seller_id, sku, marketplace_ids, issue_locale=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_listings_item(self):
        seller_id = random.random()
        sku = random.random()
        marketplace_ids = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_listings_item"), "200")
        response = self.api.get_listings_item_with_http_info(seller_id, sku, marketplace_ids, issue_locale=None, included_data=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_patch_listings_item(self):
        seller_id = random.random()
        sku = random.random()
        marketplace_ids = random.random()
        body = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("patch_listings_item"), "200")
        response = self.api.patch_listings_item_with_http_info(seller_id, sku, marketplace_ids, body, included_data=None, mode=None, issue_locale=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_put_listings_item(self):
        seller_id = random.random()
        sku = random.random()
        marketplace_ids = random.random()
        body = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("put_listings_item"), "200")
        response = self.api.put_listings_item_with_http_info(seller_id, sku, marketplace_ids, body, included_data=None, mode=None, issue_locale=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_search_listings_items(self):
        seller_id = random.random()
        marketplace_ids = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("search_listings_items"), "200")
        response = self.api.search_listings_items_with_http_info(seller_id, marketplace_ids, issue_locale=None, included_data=None, identifiers=None, identifiers_type=None, variation_parent_sku=None, package_hierarchy_sku=None, created_after=None, created_before=None, last_updated_after=None, last_updated_before=None, with_issue_severity=None, with_status=None, without_status=None, sort_by=None, sort_order=None, page_size=None, page_token=None)
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