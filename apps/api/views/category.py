from django.core.paginator import Paginator
from rest_framework.views import APIView

from apps.api.models import Category
from apps.api.serializers import CategorySerializer
from utils.helper import parseBool
from utils.resp import CustomResp


class CategoryAPIView(APIView):
    def get(self, request):
        try:
            params = {
                "page": int(request.query_params.get("page", "1")),
                "limit": int(request.query_params.get("limit", "10")),
                "show_all": request.query_params.get("show_all"),
            }
            if params["show_all"] not in ["None", None, "", "all"]:
                params["show_all"] = parseBool(params["show_all"])
        except Exception as e:
            print(f"error: {e}")
            return CustomResp(
                error=True,
                message="invalid query paramters",
                error_detail=str(e),
                status_code=400,
            )

        categories = Category.objects.all()
        if not params["show_all"]:
            paginator = Paginator(categories, params["limit"])
            results = paginator.get_page(params["page"])
            serializer = CategorySerializer(results, many=True)
            return CustomResp(
                data=serializer.data,
                additional_field={
                    "pagination_meta": {
                        "total_page": paginator.num_pages,
                        "total_data": paginator.count,
                        "current_page": params["page"],
                        "limit": params["limit"],
                        "has_next": results.has_next(),
                        "has_prev": results.has_previous(),
                    }
                },
            )
        else:
            serializer = CategorySerializer(categories, many=True)
            return CustomResp(
                data=serializer.data,
                additional_field={
                    "pagination_meta": {
                        "total_page": 0,
                        "total_data": len(categories),
                        "current_page": 0,
                        "limit": 0,
                        "has_next": False,
                        "has_prev": False,
                    }
                },
            )
