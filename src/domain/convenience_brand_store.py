import json

from typing import Protocol, List

from pydantic import field_validator, BaseModel
from pydantic_geojson import MultiPolygonModel, PointModel


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
    geometry: MultiPolygonModel

    @field_validator("geometry", mode="before")
    @classmethod
    def transform(cls, raw: str) -> dict:
        v = json.loads(raw)
        return v


# Repository
class ConvenienceBrandStoreRepository(Protocol):
    def get_brand_stores(self) -> List[BrandStore]:
        pass

    def get_populations(self) -> List[Population]:
        pass


# Usecase
class ConvenienceBrandStoreUsecase(Protocol):
    def get_brand_stores(self) -> List[BrandStore]:
        pass

    def get_populations(self) -> List[Population]:
        pass