import json

from typing import List, Protocol, Optional, Tuple, Union

from pydantic import field_validator, BaseModel
from pydantic_geojson import MultiPolygonModel, PolygonModel


# Entity
class GeomKabkotaPizza(BaseModel):
    ogc_fid: int
    pt_id: int
    seg_id: int
    ring_id: int
    geometry: Union[MultiPolygonModel, PolygonModel]

    @field_validator("geometry", mode="before")
    @classmethod
    def transform(cls, raw: str) -> dict:
        v = json.loads(raw)
        return v


class GeomIndonesiaKelurahan(BaseModel):
    ogc_fid: int
    id: int
    desa_seq: Optional[int] = None
    desa: str
    density: Optional[float] = None
    kecamatan_seq: Optional[int] = None
    kecamatan: str
    kabkota_seq: Optional[int] = None
    kabkota: str
    provinsi_seq: Optional[int] = None
    provinsi: str
    gid: int
    area_ha: float
    population: Optional[float] = None
    jumlah_kk: Optional[str] = None
    jumlah_penduduk: Optional[str] = None
    elevation: Optional[str] = None
    geometry: Union[MultiPolygonModel, PolygonModel]

    @field_validator("geometry", mode="before")
    @classmethod
    def transform(cls, raw: str) -> dict:
        v = json.loads(raw)
        return v


# Repository
class IndomarcoPizzaDBRepository(Protocol):
    def count_geom_kabkota_pizza(self) -> int:
        pass

    def get_geom_kabkota_pizza(self, page: int, limit: int) -> List[GeomKabkotaPizza]:
        pass

    def count_geom_indonesia_kelurahan(self) -> int:
        pass

    def get_geom_indonesia_kelurahan(self, page: int, limit: int) -> List[GeomIndonesiaKelurahan]:
        pass


# Usecase
class IndomarcoPizzaUsecase(Protocol):
    def get_geom_kabkota_pizza(self, page: int, limit: int) -> Tuple[int, List[GeomKabkotaPizza]]:
        pass

    def get_geom_indonesia_kelurahan(self, page: int, limit: int) -> Tuple[int, List[GeomIndonesiaKelurahan]]:
        pass
