import pytest

from src.helpers.api_requests_wrapper import post_request
from src.constants.API_Constants import APIConstants
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code




class TestCreateBooing(object):

    def test_create_booking_tc1(self):
        # payload = payload_create_booking()
        # print(payload)
        # payload.update({"firstname":"Vishnu" , "lastname" : "vardhan"})
        #  or
        # payload["firstname"] = "Vishhhh"
        # print(payload)


        # URL, headers, payload,
        response = post_request(url=APIConstants.create_booking_url(), auth=None, headers=common_headers_json(), payload=payload_create_booking(), in_json=False)
        print(response)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        bookingid = response.json()["bookingid"]
        print(bookingid)