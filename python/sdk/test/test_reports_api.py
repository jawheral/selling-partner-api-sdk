# coding: utf-8

from __future__ import absolute_import

import unittest
import requests
import random

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.reports_v2021_06_30.reports_api import ReportsApi

import spapi.models.reports_v2021_06_30 as models

class TestReportsApi(unittest.TestCase):
    """ReportsApi unit test stubs"""

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
        self.api = ReportsApi(client.api_client)

    def tearDown(self):
        pass

    def test_cancel_report(self):
        report_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("cancel_report"), "200")
        response = self.api.cancel_report_with_http_info(report_id)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_cancel_report_schedule(self):
        report_schedule_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("cancel_report_schedule"), "200")
        response = self.api.cancel_report_schedule_with_http_info(report_schedule_id)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_create_report(self):
        body = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("create_report"), "202")
        response = self.api.create_report_with_http_info(body)
        self.assertEqual(202, response[1])
        self.assert_valid_response_payload(202, response[0])
        pass

    def test_create_report_schedule(self):
        body = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("create_report_schedule"), "201")
        response = self.api.create_report_schedule_with_http_info(body)
        self.assertEqual(201, response[1])
        self.assert_valid_response_payload(201, response[0])
        pass

    def test_get_report(self):
        report_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_report"), "200")
        response = self.api.get_report_with_http_info(report_id)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_report_document(self):
        report_document_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_report_document"), "200")
        response = self.api.get_report_document_with_http_info(report_document_id)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_report_schedule(self):
        report_schedule_id = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_report_schedule"), "200")
        response = self.api.get_report_schedule_with_http_info(report_schedule_id)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_report_schedules(self):
        report_types = random.random()
        
        self.instruct_backend_mock(self.to_camel_case("get_report_schedules"), "200")
        response = self.api.get_report_schedules_with_http_info(report_types)
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_get_reports(self):
        
        self.instruct_backend_mock(self.to_camel_case("get_reports"), "200")
        response = self.api.get_reports_with_http_info(report_types=None, processing_statuses=None, marketplace_ids=None, page_size=None, created_since=None, created_until=None, next_token=None)
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