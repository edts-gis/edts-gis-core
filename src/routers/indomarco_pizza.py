from fastapi import APIRouter, Request
from kink import di

from src.payloads.response import (
    GeoJSONResponse,
    PaginateGeoJSONResponse
)

from src.domain.indomarco_pizza import IndomarcoPizzaUsecase


api_router = APIRouter(
    prefix = "/indomarco-pizza",
    tags = ["indomarco_pizza"]
)

# Router
@api_router.get("/geom-kabkota-pizza", response_model=PaginateGeoJSONResponse)
def get_geom_kabkota_pizza(r: Request, page: int = 1, limit: int = 2000):
    u_ip = di[IndomarcoPizzaUsecase]

    count_geom_kabkota_pizza, geom_kabkota_pizza = u_ip.get_geom_kabkota_pizza(page, limit)
    response = PaginateGeoJSONResponse.from_result(
        page = page,
        page_size = len(geom_kabkota_pizza),
        total_page = (count_geom_kabkota_pizza // limit) + 1,
        total_data = count_geom_kabkota_pizza,
        current_url = str(r.url),
        data = GeoJSONResponse.from_db_model(
            name = "geom_kabkota_pizza",
            crs = "CRS84",
            data = geom_kabkota_pizza
        )
    )
    return response


@api_router.get("/geom-indonesia-kelurahan", response_model=PaginateGeoJSONResponse)
def get_geom_indonesia_kelurahan(r: Request, page: int = 1, limit: int = 2000):
    u_ip = di[IndomarcoPizzaUsecase]

    count_geom_indonesia_kelurahan, geom_indonesia_kelurahan = u_ip.get_geom_indonesia_kelurahan(page, limit)
    response = PaginateGeoJSONResponse.from_result(
        page = page,
        page_size = len(geom_indonesia_kelurahan),
        total_page = (count_geom_indonesia_kelurahan // limit) + 1,
        total_data = count_geom_indonesia_kelurahan,
        current_url = str(r.url),
        data = GeoJSONResponse.from_db_model(
            name = "indonesia_kelurahan",
            crs = "CRS84",
            data = geom_indonesia_kelurahan
        )
    )
    return response
