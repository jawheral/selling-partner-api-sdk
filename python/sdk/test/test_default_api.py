# coding: utf-8

from __future__ import absolute_import

import unittest
import requests
import random

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.finances_v0.default_api import DefaultApi

import spapi.models.finances_v0 as models

class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

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
        self.api = DefaultApi(client.api_client)

    def tearDown(self):
        pass

    def test_list_financial_event_groups(self):
        
        self.instruct_backend_mock(self.to_camel_case("list_financial_event_groups"), "200")
        response = self.api.list_financial_event_groups_with_http_info(max_results_per_page=None, financial_event_group_started_before=None, financial_event_group_started_after=None, next_token=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_list_financial_events(self):
        
        self.instruct_backend_mock(self.to_camel_case("list_financial_events"), "200")
        response = self.api.list_financial_events_with_http_info(max_results_per_page=None, posted_after=None, posted_before=None, next_token=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_list_financial_events_by_group_id(self):
        event_group_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("list_financial_events_by_group_id"), "200")
        response = self.api.list_financial_events_by_group_id_with_http_info(event_group_id, max_results_per_page=None, posted_after=None, posted_before=None, next_token=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_list_financial_events_by_order_id(self):
        order_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("list_financial_events_by_order_id"), "200")
        response = self.api.list_financial_events_by_order_id_with_http_info(order_id, max_results_per_page=None, next_token=None)
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