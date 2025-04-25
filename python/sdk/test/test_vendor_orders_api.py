# coding: utf-8

from __future__ import absolute_import

import unittest
import requests
import random

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.vendor_orders_v1.vendor_orders_api import VendorOrdersApi

import spapi.models.vendor_orders_v1 as models

class TestVendorOrdersApi(unittest.TestCase):
    """VendorOrdersApi unit test stubs"""

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
        self.api = VendorOrdersApi(client.api_client)

    def tearDown(self):
        pass

    def test_get_purchase_order(self):
        purchase_order_number = self._get_random_value("str")
        
        self.instruct_backend_mock(self.to_camel_case("get_purchase_order"), "200")
        response = self.api.get_purchase_order_with_http_info(purchase_order_number)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_purchase_orders(self):
        
        self.instruct_backend_mock(self.to_camel_case("get_purchase_orders"), "200")
        response = self.api.get_purchase_orders_with_http_info(, , , , , , , , , , , )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_purchase_orders_status(self):
        
        self.instruct_backend_mock(self.to_camel_case("get_purchase_orders_status"), "200")
        response = self.api.get_purchase_orders_status_with_http_info(, , , , , , , , , , , , )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_submit_acknowledgement(self):
        body = self._get_random_value("SubmitAcknowledgementRequest")
        
        self.instruct_backend_mock(self.to_camel_case("submit_acknowledgement"), "202")
        response = self.api.submit_acknowledgement_with_http_info(body)
        self.assertEqual(202, response[1])
        self.assert_valid_response_payload(202, response[0])
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