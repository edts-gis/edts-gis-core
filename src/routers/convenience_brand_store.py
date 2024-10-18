from fastapi import APIRouter, Request
from kink import di

from src.payloads.response import (
    GeoJSONResponse,
    PaginateGeoJSONResponse
)

from src.domain.convenience_brand_store import ConvenienceBrandStoreUsecase


api_router = APIRouter(
    prefix = "/convenience-brand-store",
    tags = ["convenience_brand_store"]
)

# Router
@api_router.get("/brand-stores", response_model=PaginateGeoJSONResponse)
def get_brand_store(r: Request, page: int = 1, limit: int = 500):
    u_ip = di[ConvenienceBrandStoreUsecase]

    count_brand_stores, brand_stores = u_ip.get_brand_stores(page, limit)
    response = PaginateGeoJSONResponse.from_result(
        page = page,
        page_size = len(brand_stores),
        total_page = (count_brand_stores // limit) + 1,
        total_data = count_brand_stores,
        current_url = str(r.url),
        data = GeoJSONResponse.from_db_model(
            name = "brand_stores",
            crs = "CRS84",
            data = brand_stores
        )
    )
    return response


@api_router.get("/populations", response_model=PaginateGeoJSONResponse)
def get_population(r: Request, page: int = 1, limit: int = 500):
    u_ip = di[ConvenienceBrandStoreUsecase]
    
    count_populations, populations = u_ip.get_populations(page, limit)
    response = PaginateGeoJSONResponse.from_result(
        page = page,
        page_size = len(populations),
        total_page = (count_populations // limit) + 1,
        total_data = count_populations,
        current_url = str(r.url),
        data = GeoJSONResponse.from_db_model(
            name = "populations",
            crs = "CRS84",
            data = populations
        )
    )
    return response
