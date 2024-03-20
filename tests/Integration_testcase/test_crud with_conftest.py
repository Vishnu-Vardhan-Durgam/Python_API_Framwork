import pytest
import requests

from src.helpers.api_requests_wrapper import post_request, put_request, get_request
from src.constants.API_Constants import APIConstants
from src.helpers.utils import common_headers_json, common_headers_for_put_delete_patch
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code


def test_update_booking(self, create_token, create_booking):  # Token and Booking ID/Basic auth from Create Booking and Token call
    # print(test_create_booking)
    bookingID = create_booking
    put_url = APIConstants.create_booking_url() + "/" + str(bookingID)
    response = put_request(url=put_url, auth=None, headers=common_headers_for_put_delete_patch(),
                           payload=payload_create_booking(), in_json=False)
    print(response.json())


def test_get_booking(self, create_token, create_booking):
    bookingID = create_booking
    get_url = APIConstants.create_booking_url() + "/" + str(bookingID)
    response = get_request(url=get_url, auth=None, in_json=False)
    print(response.json())


def test_delete_booking(self, create_token, create_booking):  # Token and Booking ID/Basic auth from Create Booking and Token call
    bookingID = create_booking
    delete_url = APIConstants.create_booking_url() + "/" + str(bookingID)
    response = put_request(url=delete_url, auth=None, headers=common_headers_for_put_delete_patch(),
                           payload=None, in_json=False)
    print(response.json())
