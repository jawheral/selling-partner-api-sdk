# coding: utf-8

from __future__ import absolute_import

import unittest
import requests
import random

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.product_fees_v0.fees_api import FeesApi

import spapi.models.product_fees_v0 as models

class TestFeesApi(unittest.TestCase):
    """FeesApi unit test stubs"""

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
        self.api = FeesApi(client.api_client)

    def tearDown(self):
        pass

    def test_get_my_fees_estimate_for_asin(self):
        asin = random.random()
        body = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_my_fees_estimate_for_asin"), "200")
        response = self.api.get_my_fees_estimate_for_asin_with_http_info(asin, body)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_my_fees_estimate_for_sku(self):
        seller_sku = random.random()
        body = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_my_fees_estimate_for_sku"), "200")
        response = self.api.get_my_fees_estimate_for_sku_with_http_info(seller_sku, body)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_my_fees_estimates(self):
        body = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_my_fees_estimates"), "200")
        response = self.api.get_my_fees_estimates_with_http_info(body)
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