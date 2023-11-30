from rest_framework.response import Response

class CustomResp(Response):
    def __init__(self, error=False, message="OK", data=None, error_detail="", status_code=200, additional_field=None, **kwargs):
        data = {
            "error": error,
            "status_code": status_code,
            "message": message,
            "error_detail": error_detail,
            "data": data
        }
        if additional_field:
            data.update(additional_field)
        super().__init__(data, status=status_code, **kwargs)