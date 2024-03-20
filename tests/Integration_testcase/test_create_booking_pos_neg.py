from src.helpers.api_requests_wrapper import post_request
from src.constants.API_Constants import APIConstants
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code

import pytest


class TestCreateBooing(object):

    @pytest.mark.postive
    def test_create_booking_tc1(self):
        # URL, headers, payload,
        response = post_request(url=APIConstants.create_booking_url(), auth=None, headers=common_headers_json(),
                                payload=payload_create_booking(), in_json=False)
        print(response)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        bookingid = response.json()["bookingid"]
        print(bookingid)

    @pytest.mark.negative
    def test_create_booking_tc2(self):
        # URL, headers, payload,
        response = post_request(url=APIConstants.create_booking_url(), auth=None, headers=common_headers_json(),
                                payload=None, in_json=False)  # payload ({}=500 and None=400)
        print(response)
        # verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 400)
        # bookingid = response.json()["bookingid"]
        # print(bookingid)
