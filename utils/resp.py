from rest_framework.response import Response

class CustomResp(Response):
    def __init__(self, error=False, message="OK", data=None, error_detail="", status_code=200, **kwargs):
        data = {
            "error": error,
            "status_code": status_code,
            "message": message,
            "error_detail": error_detail,
            "data": data
        }
        super().__init__(data, status=status_code, **kwargs)