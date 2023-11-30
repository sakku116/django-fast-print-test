from pydantic import BaseModel

class PostProductCreationReq(BaseModel):
    nama_produk: str
    harga: int
    id_kategori: int
    id_status: int