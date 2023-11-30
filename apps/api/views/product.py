import json

from django.core.paginator import Paginator
from rest_framework import permissions
from rest_framework.views import APIView

from apps.api.models import Category, Product, Status
from apps.api.schemas.req import products as products_req
from apps.api.serializers import ProductSerializer, CategorySerializer, StatusSerializer
from utils.helper import parseBool
from utils.resp import CustomResp


class ProductApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            params = {
                "available": request.query_params.get("available"),
                "page": int(request.query_params.get("page", "1")),
                "limit": int(request.query_params.get("limit", "10")),
            }
            if params["available"] not in ["None", "", None, "all"]:
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
            filters["status__nama_status"] = (
                "bisa dijual" if params["available"] else "tidak bisa dijual"
            )

        products = Product.objects.select_related("kategori", "status").order_by("-created_at").filter(**filters).all()
        paginator = Paginator(products, params["limit"])
        results = paginator.get_page(params["page"])
        serializer = ProductSerializer(results, many=True)

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
            status_code=200,
        )

    def post(self, request, *args, **kwargs):
        try:
            payload = products_req.PostProductCreationReq(**json.loads(request.body))
        except Exception as e:
            print(f"error: {e}")
            return CustomResp(
                error=True,
                message="invalid payload",
                error_detail=str(e),
                status_code=400,
            )

        try:
            category = Category.objects.get(id_kategori=payload.id_kategori)
        except Category.DoesNotExist as e:
            return CustomResp(error=True, message="category not found", status_code=400)
        except Exception as e:
            print(f"error: {e}")
            raise CustomResp(error=True, message="internal server error", error_detail=str(e), status_code=500)

        try:
            status = Status.objects.get(id_status=payload.id_status)
        except Status.DoesNotExist as e:
            return CustomResp(error=True, message="category not found", status_code=400)
        except Exception as e:
            print(f"error: {e}")
            raise CustomResp(error=True, message="internal server error", error_detail=str(e), status_code=500)

        new_product = Product.objects.create(
            nama_produk=payload.nama_produk,
            harga=payload.harga,
            kategori=category,
            status=status,
        )

        serializer = ProductSerializer(new_product)
        return CustomResp(error=False, message="product created", data=serializer.data, status_code=200)

class ProductDetailApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, product_id: str, *args, **kwargs):
        try:
            product = Product.objects.select_related("kategori", "status").get(id_produk=product_id)
        except Product.DoesNotExist as e:
            return CustomResp(error=True, message="product not found", status_code=400)

        serializer = ProductSerializer(product)
        return CustomResp(data=serializer.data, status_code=200)

    def patch(self, request, product_id: str, *args, **kwargs):
        try:
            payload = products_req.PatchProductUpdationReq(**json.loads(request.body))
        except Exception as e:
            print(f"error: {e}")
            return CustomResp(
                error=True,
                message="invalid payload",
                error_detail=str(e),
                status_code=400,
            )

        try:
            existing_obj = Product.objects.get(id_produk=product_id)
        except Product.DoesNotExist as e:
            return CustomResp(error=True, message="product not found", status_code=400)

        if payload.nama_produk:
            existing_obj.nama_produk = payload.nama_produk
        if payload.harga:
            existing_obj.harga = payload.harga
        if payload.id_kategori:
            try:
                category = Category.objects.get(id_kategori=payload.id_kategori)
            except Category.DoesNotExist as e:
                return CustomResp(error=True, message="category not found", status_code=400)
            except Exception as e:
                print(f"error: {e}")
                raise CustomResp(error=True, message="internal server error", error_detail=str(e), status_code=500)
            existing_obj.kategori = category
        if payload.id_status:
            try:
                status = Status.objects.get(id_status=payload.id_status)
            except Status.DoesNotExist as e:
                return CustomResp(error=True, message="status not found", status_code=400)
            except Exception as e:
                print(f"error: {e}")
                raise CustomResp(error=True, message="internal server error", error_detail=str(e), status_code=500)
            existing_obj.status = status

        existing_obj.save()

        serializer = ProductSerializer(existing_obj)
        return CustomResp(error=False, message="product updated", data=serializer.data, status_code=200)

    def delete(self, request, product_id: str, *args, **kwargs):
        try:
            existing_obj = Product.objects.get(id_produk=product_id)
        except Product.DoesNotExist as e:
            return CustomResp(error=True, message="product not found", status_code=400)

        existing_obj.delete()
        return CustomResp(error=False, message="product deleted", status_code=200)