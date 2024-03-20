# HTTP status verification

def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, "Expected HTTP status code"+str(expect_data)

def verify_json_key_for_not_null(key):
    assert key !=0,"key is not empty"+key
    assert key > 0,"key is not Zero"

def verify_response_key_should_not_be_none(key):
    assert key is not None

def verify_repsonse_time():
    pass

# common verification
# HTTP status code
# Headers
# Data verification
# json scema