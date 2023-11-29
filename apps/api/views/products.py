from django.core.paginator import Paginator
from rest_framework import permissions
from rest_framework.views import APIView

from apps.api.models import Product
from apps.api.serializers import ProductSerializer
from utils.helper import parseBool
from utils.resp import CustomResp


class ProductApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            params = {
                "available": request.query_params.get("available"),
                "page": int(request.query_params.get("page", "1")),
                "limit": int(request.query_params.get("limit", "10")),
            }
            if params["available"] not in ["None", ""]:
                params["available"] = parseBool(params["available"])
        except Exception as e:
            print(f"error: {e}")
            return CustomResp(
                error=True,
                message="invalid query paramters",
                error_detail=str(e),
                status_code=400,
            )

        filters = {}
        if type(params["available"]) == bool:
            filters["kategori__nama_kategori"] = (
                "bisa djual" if params["available"] else "tidak bisa dijual"
            )

        products = Product.objects.filter(**filters).all()
        paginator = Paginator(products, params["limit"])
        results = paginator.get_page(params["page"])
        serializer = ProductSerializer(results, many=True)

        return CustomResp(data=serializer.data, status_code=200)
