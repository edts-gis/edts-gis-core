from fastapi import APIRouter
from kink import di

from src.payloads.response import (
    GeoJSONResponse
)

from src.domain.convenience_brand_store import ConvenienceBrandStoreUsecase


API_GROUP = "convenience_brand_store"

api_router = APIRouter(
    prefix = "/convenience-brand-store",
    tags = ["convenience_brand_store"]
)

# Router
@api_router.get("/brand-stores", response_model=GeoJSONResponse)
def get_brand_store():
    u_ip = di[ConvenienceBrandStoreUsecase]

    brand_stores = u_ip.get_brand_stores()
    response = GeoJSONResponse.from_db_dict(
        name = "brand_stores",
        crs = "CRS84",
        data = list(map(lambda d: d.model_dump(), brand_stores))
    )
    return response


@api_router.get("/populations", response_model=GeoJSONResponse)
def get_population():
    u_ip = di[ConvenienceBrandStoreUsecase]

    populations = u_ip.get_populations()
    response = GeoJSONResponse.from_db_dict(
        name = "populations",
        crs = "CRS84",
        data = list(map(lambda d: d.model_dump(), populations))
    )
    return response
