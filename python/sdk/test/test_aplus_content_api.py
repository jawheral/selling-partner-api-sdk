# coding: utf-8

from __future__ import absolute_import

import unittest
import requests
import random

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.apluscontent_v2020_11_01.aplus_content_api import AplusContentApi

import spapi.models.apluscontent_v2020_11_01 as models

class TestAplusContentApi(unittest.TestCase):
    """AplusContentApi unit test stubs"""

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
        self.api = AplusContentApi(client.api_client)

    def tearDown(self):
        pass

    def test_create_content_document(self):
        marketplace_id = random.random()
        post_content_document_request = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("create_content_document"), "200")
        response = self.api.create_content_document_with_http_info(marketplace_id, post_content_document_request)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_content_document(self):
        content_reference_key = random.random()
        marketplace_id = random.random()
        included_data_set = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_content_document"), "200")
        response = self.api.get_content_document_with_http_info(content_reference_key, marketplace_id, included_data_set)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_list_content_document_asin_relations(self):
        content_reference_key = random.random()
        marketplace_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("list_content_document_asin_relations"), "200")
        response = self.api.list_content_document_asin_relations_with_http_info(content_reference_key, marketplace_id, included_data_set=None, asin_set=None, page_token=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_post_content_document_approval_submission(self):
        content_reference_key = random.random()
        marketplace_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("post_content_document_approval_submission"), "200")
        response = self.api.post_content_document_approval_submission_with_http_info(content_reference_key, marketplace_id)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_post_content_document_asin_relations(self):
        content_reference_key = random.random()
        marketplace_id = random.random()
        post_content_document_asin_relations_request = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("post_content_document_asin_relations"), "200")
        response = self.api.post_content_document_asin_relations_with_http_info(content_reference_key, marketplace_id, post_content_document_asin_relations_request)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_post_content_document_suspend_submission(self):
        content_reference_key = random.random()
        marketplace_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("post_content_document_suspend_submission"), "200")
        response = self.api.post_content_document_suspend_submission_with_http_info(content_reference_key, marketplace_id)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_search_content_documents(self):
        marketplace_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("search_content_documents"), "200")
        response = self.api.search_content_documents_with_http_info(marketplace_id, page_token=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_search_content_publish_records(self):
        marketplace_id = random.random()
        asin = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("search_content_publish_records"), "200")
        response = self.api.search_content_publish_records_with_http_info(marketplace_id, asin, page_token=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_update_content_document(self):
        content_reference_key = random.random()
        marketplace_id = random.random()
        post_content_document_request = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("update_content_document"), "200")
        response = self.api.update_content_document_with_http_info(content_reference_key, marketplace_id, post_content_document_request)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_validate_content_document_asin_relations(self):
        marketplace_id = random.random()
        post_content_document_request = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("validate_content_document_asin_relations"), "200")
        response = self.api.validate_content_document_asin_relations_with_http_info(marketplace_id, post_content_document_request, asin_set=None)
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