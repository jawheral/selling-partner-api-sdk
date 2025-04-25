# coding: utf-8

from __future__ import absolute_import

import unittest
import requests
import random

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.product_pricing_v0.product_pricing_api import ProductPricingApi

import spapi.models.product_pricing_v0 as models

class TestProductPricingApi(unittest.TestCase):
    """ProductPricingApi unit test stubs"""

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
        self.api = ProductPricingApi(client.api_client)

    def tearDown(self):
        pass

    def test_get_competitive_pricing(self):
        marketplace_id = self._get_random_value("str")
        item_type = self._get_random_value("str")
        
        self.instruct_backend_mock(self.to_camel_case("get_competitive_pricing"), "200")
        response = self.api.get_competitive_pricing_with_http_info(marketplace_id, item_type, asins={}, skus={}, customer_type={})
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_item_offers(self):
        marketplace_id = self._get_random_value("str")
        item_condition = self._get_random_value("str")
        asin = self._get_random_value("str")
        
        self.instruct_backend_mock(self.to_camel_case("get_item_offers"), "200")
        response = self.api.get_item_offers_with_http_info(marketplace_id, item_condition, asin, customer_type={})
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_item_offers_batch(self):
        get_item_offers_batch_request_body = self._get_random_value("GetItemOffersBatchRequest")
        
        self.instruct_backend_mock(self.to_camel_case("get_item_offers_batch"), "200")
        response = self.api.get_item_offers_batch_with_http_info(get_item_offers_batch_request_body)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_listing_offers(self):
        marketplace_id = self._get_random_value("str")
        item_condition = self._get_random_value("str")
        seller_sku = self._get_random_value("str")
        
        self.instruct_backend_mock(self.to_camel_case("get_listing_offers"), "200")
        response = self.api.get_listing_offers_with_http_info(marketplace_id, item_condition, seller_sku, customer_type={})
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_listing_offers_batch(self):
        get_listing_offers_batch_request_body = self._get_random_value("GetListingOffersBatchRequest")
        
        self.instruct_backend_mock(self.to_camel_case("get_listing_offers_batch"), "200")
        response = self.api.get_listing_offers_batch_with_http_info(get_listing_offers_batch_request_body)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_pricing(self):
        marketplace_id = self._get_random_value("str")
        item_type = self._get_random_value("str")
        
        self.instruct_backend_mock(self.to_camel_case("get_pricing"), "200")
        response = self.api.get_pricing_with_http_info(marketplace_id, item_type, asins={}, skus={}, item_condition={}, offer_type={})
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass


    def instruct_backend_mock(self, response: str, code: str) -> None:
        url = f"{self.mock_server_endpoint}/response/{response}/code/{code}"
        requests.post(url)

    def _get_random_value(self, data_type):
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