# coding: utf-8

from __future__ import absolute_import

import unittest
import requests
import rstr

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.solicitations_v1.solicitations_api import SolicitationsApi

import spapi.models.solicitations_v1 as models

class TestSolicitationsApi(unittest.TestCase):
    """SolicitationsApi unit test stubs"""

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
        self.api = SolicitationsApi(client.api_client)

    def tearDown(self):
        pass

    def test_create_product_review_and_seller_feedback_solicitation(self):
        amazon_order_id = self._get_random_value("str", None)
        marketplace_ids = [self._get_random_value("List[str]") for _ in range(1)]
        
        self.instruct_backend_mock(self.to_camel_case("create_product_review_and_seller_feedback_solicitation"), "201")
        response = self.api.create_product_review_and_seller_feedback_solicitation_with_http_info(amazon_order_id, marketplace_ids, )
        self.assertEqual(201, response[1])
        self.assert_valid_response_payload(201, response[0])
        pass

    def test_get_solicitation_actions_for_order(self):
        amazon_order_id = self._get_random_value("str", None)
        marketplace_ids = [self._get_random_value("List[str]") for _ in range(1)]
        
        self.instruct_backend_mock(self.to_camel_case("get_solicitation_actions_for_order"), "200")
        response = self.api.get_solicitation_actions_for_order_with_http_info(amazon_order_id, marketplace_ids, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass


    def instruct_backend_mock(self, response: str, code: str) -> None:
        url = f"{self.mock_server_endpoint}/response/{response}/code/{code}"
        ## handle same api operation name exceptions
        if "vendor" in api.solicitations_v1 and response == "getOrder":
            url += f"?qualifier=Vendor"
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