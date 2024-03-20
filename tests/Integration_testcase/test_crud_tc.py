from src.constants.API_Constants import BASE_URL, APIConstants, base_url

import requests  # Optional


def test_crud():
    print(BASE_URL)

    url_direct_func = base_url()
    print(url_direct_func)

    requests.get(url_direct_func)  # Optional

    url_class = APIConstants().base_url()
    # url_class = APIConstants.base_url() # with @staticmethod and (self)
    print(url_class)
