# to make the requests like POST , PUT , PATCH and DELETE
import json

import requests

# HTTP methods - Generic functions

def get_request(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:
        return response.json()
    return response

def post_request(url, auth, payload, headers, in_json):
    post_response = requests.post(url=url, auth=auth,headers=headers, data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response

def patch_request(url,auth,payload,headers,in_json):
    patch_response_data = requests.patch(url=url, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data

def put_request(url, auth, payload, headers, in_json):
    put_response_data = requests.put(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return put_response_data.json()
    return put_response_data

def delete_request(url, auth, headers, in_json):
    delete_response_data = requests.delete(url=url, headers=headers, auth=auth)
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data
