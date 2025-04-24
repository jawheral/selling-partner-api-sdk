# coding: utf-8

from __future__ import absolute_import

import unittest
import requests
import random

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.fba_eligibility_v1.fba_inbound_api import FbaInboundApi

import spapi.models.fba_eligibility_v1 as models

class TestFbaInboundApi(unittest.TestCase):
    """FbaInboundApi unit test stubs"""

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
        self.api = FbaInboundApi(client.api_client)

    def tearDown(self):
        pass

    def test_get_item_eligibility_preview(self):
        asin = random.random()
        program = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_item_eligibility_preview"), "200")
        response = self.api.get_item_eligibility_preview_with_http_info(asin, program, marketplace_ids=None)
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