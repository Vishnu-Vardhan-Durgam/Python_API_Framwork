import pytest
import requests

from src.helpers.api_requests_wrapper import post_request, put_request, get_request
from src.constants.API_Constants import APIConstants
from src.helpers.utils import common_headers_json, common_headers_for_put_delete_patch
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code


@pytest.fixture()
def create_token(self):
    response = post_request(
        url=APIConstants.url_create_token(),
        headers=common_headers_json(),
        auth=None,
        payload=payload_create_token(), in_json=False
    )
    print(response)
    verify_http_status_code(response, 200)
    token = response.json()["token"]
    verify_response_key_should_not_be_none(token)
    token = response.json()["token"]
    print(token)


@pytest.fixture()
def create_booking(self):
    # URL, headers, payload,
    response = post_request(url=APIConstants.create_booking_url(), auth=None, headers=common_headers_json(),
                            payload=payload_create_booking(), in_json=False)
    print(response)
    verify_response_key_should_not_be_none(response.json()["bookingid"])
    verify_http_status_code(response, 200)
    bookingid = response.json()["bookingid"]
    print(bookingid)
    return bookingid
