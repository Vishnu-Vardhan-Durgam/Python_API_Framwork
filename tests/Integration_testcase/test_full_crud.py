import pytest

from src.helpers.api_requests_wrapper import post_request,put_request,get_request
from src.constants.API_Constants import APIConstants
from src.helpers.utils import common_headers_json, common_headers_for_put_delete_patch
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code



class TestCreateBooing(object):

    @pytest.fixture()
    def test_create_token(self):
    # def create_token(self): --> can be normal function as well

        response = post_request(
            url=APIConstants.url_create_token(),
            headers = common_headers_json(),
            auth = None,
            payload =payload_create_token(), in_json=False
        )
        print(response)
        verify_http_status_code(response,200)
        token = response.json()["token"]
        verify_response_key_should_not_be_none(token)
        print(token)

    @pytest.fixture()
    def test_create_booking(self):
    # def create_booking(self): --> can be normal function as well

        # URL, headers, payload,
        response = post_request(url=APIConstants.create_booking_url(), auth=None, headers=common_headers_json(),
                                payload=payload_create_booking(), in_json=False)
        print(response)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        return bookingid


    def test_update_booking(self, test_create_token,test_create_booking): # Token and Booking ID from Create Booking and Token call
        # print(test_create_token)
        # print(test_create_booking)
        bookingID = test_create_booking
        put_url = APIConstants.create_booking_url() + "/"+str(bookingID)
        response = put_request(url=put_url, auth=None, headers=common_headers_for_put_delete_patch(),
                               payload=payload_create_booking(), in_json=False)
        print(response.json())


    def test_get_booking(self,test_create_token,test_create_booking):
        bookingID = test_create_booking
        get_url = APIConstants.create_booking_url() + "/"+str(bookingID)
        response = get_request(url=get_url, auth = None, in_json=False)
        print(response.json())



    def test_delete_booking(self,test_create_token,test_create_booking): # Token and Booking ID from Create Booking and Token call
        bookingID = test_create_booking
        delete_url = APIConstants.create_booking_url() + "/"+str(bookingID)
        response = put_request(url=delete_url, auth=None, headers=common_headers_for_put_delete_patch(),
                               payload=None, in_json=False)
        print(response.json())

