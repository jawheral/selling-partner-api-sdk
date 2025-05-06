# coding: utf-8

from __future__ import absolute_import

import requests
import rstr

from spapi.auth.credentials import SPAPIConfig
from spapi.client import SPAPIClient
from spapi.api.appintegrations_v2024_04_01.app_integrations_api import AppIntegrationsApi

import spapi.models.appintegrations_v2024_04_01 as models

class TestAppIntegrationsApi(unittest.TestCase):
    """AppIntegrationsApi unit test stubs"""

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
        self.api = AppIntegrationsApi(client.api_client)

    def tearDown(self):
        pass

    def test_create_notification(self):
        body = self._get_random_value("CreateNotificationRequest", None)
        
        self.instruct_backend_mock(self.to_camel_case("create_notification"), "200")
        response = self.api.create_notification_with_http_info(body, )
        self.assertEqual(200, response[1])
        self.assert_valid_response_payload(200, response[0])
        pass

    def test_delete_notifications(self):
        body = self._get_random_value("DeleteNotificationsRequest", None)
        
        self.instruct_backend_mock(self.to_camel_case("delete_notifications"), "204")
        response = self.api.delete_notifications_with_http_info(body, )
        pass

    def test_record_action_feedback(self):
        notification_id = self._get_random_value("str", None)
        body = self._get_random_value("RecordActionFeedbackRequest", None)
        
        self.instruct_backend_mock(self.to_camel_case("record_action_feedback"), "204")
        response = self.api.record_action_feedback_with_http_info(notification_id, body, )
        pass


    def instruct_backend_mock(self, response: str, code: str) -> None:
        url = f"{self.mock_server_endpoint}/response/{response}/code/{code}"
        ## handle same api operation name exceptions
        if "vendor" in "api.appintegrations_v2024_04_01" and response == "getOrder":
            url += f"?qualifier=Vendor"
        if "fulfillment_inbound" in "api.appintegrations_v2024_04_01" and response == "getShipment":
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