from pydantic import BaseModel

class PostProductCreationReq(BaseModel):
    nama_produk: str
    harga: int
    id_kategori: int
    id_status: int

class PatchProductUpdationReq(BaseModel):
    nama_produk: str = None
    harga: int = None
    id_kategori: int = None
    id_status: int = None