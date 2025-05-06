# coding: utf-8

from __future__ import absolute_import

import requests
import rstr

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
        seller_id = self._get_random_value("str", None)
        sku = self._get_random_value("str", None)
        marketplace_ids = [self._get_random_value("List[str]") for _ in range(1)]
        
        self.instruct_backend_mock(self.to_camel_case("delete_listings_item"), "200")
        response = self.api.delete_listings_item_with_http_info(seller_id, sku, marketplace_ids, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_listings_item(self):
        seller_id = self._get_random_value("str", None)
        sku = self._get_random_value("str", None)
        marketplace_ids = [self._get_random_value("List[str]") for _ in range(1)]
        
        self.instruct_backend_mock(self.to_camel_case("get_listings_item"), "200")
        response = self.api.get_listings_item_with_http_info(seller_id, sku, marketplace_ids, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_patch_listings_item(self):
        seller_id = self._get_random_value("str", None)
        sku = self._get_random_value("str", None)
        marketplace_ids = [self._get_random_value("List[str]") for _ in range(1)]
        body = self._get_random_value("ListingsItemPatchRequest", None)
        
        self.instruct_backend_mock(self.to_camel_case("patch_listings_item"), "200")
        response = self.api.patch_listings_item_with_http_info(seller_id, sku, marketplace_ids, body, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_put_listings_item(self):
        seller_id = self._get_random_value("str", None)
        sku = self._get_random_value("str", None)
        marketplace_ids = [self._get_random_value("List[str]") for _ in range(1)]
        body = self._get_random_value("ListingsItemPutRequest", None)
        
        self.instruct_backend_mock(self.to_camel_case("put_listings_item"), "200")
        response = self.api.put_listings_item_with_http_info(seller_id, sku, marketplace_ids, body, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_search_listings_items(self):
        seller_id = self._get_random_value("str", None)
        marketplace_ids = [self._get_random_value("List[str]") for _ in range(1)]
        
        self.instruct_backend_mock(self.to_camel_case("search_listings_items"), "200")
        response = self.api.search_listings_items_with_http_info(seller_id, marketplace_ids, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass


    def instruct_backend_mock(self, response: str, code: str) -> None:
        url = f"{self.mock_server_endpoint}/response/{response}/code/{code}"
        ## handle same api operation name exceptions
        if "vendor" in "api.listings_items_v2021_08_01" and response == "getOrder":
            url += f"?qualifier=Vendor"
        if "fulfillment_inbound" in "api.listings_items_v2021_08_01" and response == "getShipment":
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