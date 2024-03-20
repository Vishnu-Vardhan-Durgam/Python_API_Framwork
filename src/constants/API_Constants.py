# Add your constants here

# # 1st method - Direct constant
# BASE_URL = "https://restful-booker.herokuapp.com"
#
#
# # 2nd method - Function constant
# def base_url():
#     return "https://restful-booker.herokuapp.com"
#
#
# def create_booking_url():
#     return "https://restful-booker.herokuapp.com/booking"
#
#
# def url_create_token():
#     return "https://restful-booker.herokuapp.com/auth"


# # Update , PUT, PATCH ,DELETE -booking ID
#
# def put_patch_delete_url(booking_id):
#     return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
#

# 3rd method - class constant
class APIConstants(object):

    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def create_booking_url():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # Update , PUT, PATCH ,DELETE -booking ID

    @staticmethod
    def put_patch_delete_url(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
