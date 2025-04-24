# coding: utf-8

from __future__ import absolute_import

import unittest
import requests
import random

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.invoices_v2024_06_19.invoices_api import InvoicesApi

import spapi.models.invoices_v2024_06_19 as models

class TestInvoicesApi(unittest.TestCase):
    """InvoicesApi unit test stubs"""

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
        self.api = InvoicesApi(client.api_client)

    def tearDown(self):
        pass

    def test_create_invoices_export(self):
        body = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("create_invoices_export"), "202")
        response = self.api.create_invoices_export_with_http_info(body)
        self.assertEqual(202, response[1])
        self.assert_valid_response_payload(202, response[0])
        pass

    def test_get_invoice(self):
        marketplace_id = random.random()
        invoice_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_invoice"), "200")
        response = self.api.get_invoice_with_http_info(marketplace_id, invoice_id)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_invoices(self):
        marketplace_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_invoices"), "200")
        response = self.api.get_invoices_with_http_info(marketplace_id, transaction_identifier_name=None, page_size=None, date_end=None, transaction_type=None, transaction_identifier_id=None, date_start=None, series=None, next_token=None, sort_order=None, invoice_type=None, statuses=None, external_invoice_id=None, sort_by=None)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_invoices_attributes(self):
        marketplace_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_invoices_attributes"), "200")
        response = self.api.get_invoices_attributes_with_http_info(marketplace_id)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_invoices_document(self):
        invoices_document_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_invoices_document"), "200")
        response = self.api.get_invoices_document_with_http_info(invoices_document_id)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_invoices_export(self):
        export_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_invoices_export"), "200")
        response = self.api.get_invoices_export_with_http_info(export_id)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_invoices_exports(self):
        marketplace_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_invoices_exports"), "200")
        response = self.api.get_invoices_exports_with_http_info(marketplace_id, date_start=None, next_token=None, page_size=None, date_end=None, status=None)
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