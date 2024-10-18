import json

from typing import List, Protocol, Tuple, Union

from pydantic import field_validator, BaseModel
from pydantic_geojson import MultiPolygonModel, PolygonModel, PointModel


# Entity
class BrandStore(BaseModel):
    ogc_fid: int
    store_company: str
    store_name: str
    province: str
    city: str
    subdistrict: str
    geometry: PointModel

    @field_validator("geometry", mode="before")
    @classmethod
    def transform(cls, raw: str) -> dict:
        v = json.loads(raw)
        return v


class Population(BaseModel):
    ogc_fid: int
    year: int
    province: str
    city: str
    population_total: int
    geometry: Union[MultiPolygonModel, PolygonModel]

    @field_validator("geometry", mode="before")
    @classmethod
    def transform(cls, raw: str) -> dict:
        v = json.loads(raw)
        return v


# Repository
class ConvenienceBrandStoreRepository(Protocol):
    def count_brand_stores(self) -> int:
        pass

    def get_brand_stores(self, page: int, limit: int) -> List[BrandStore]:
        pass

    def count_populations(self) -> int:
        pass

    def get_populations(self, page: int, limit: int) -> List[Population]:
        pass


# Usecase
class ConvenienceBrandStoreUsecase(Protocol):
    def get_brand_stores(self, page: int, limit: int) -> Tuple[int, List[BrandStore]]:
        pass

    def get_populations(self, page: int, limit: int) -> Tuple[int, List[Population]]:
        pass
