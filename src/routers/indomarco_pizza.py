from fastapi import APIRouter
from kink import di

from src.payloads.response import (
    GeoJSONResponse
)

from src.domain.indomarco_pizza import IndomarcoPizzaUsecase


API_GROUP = "indomarco_pizza"

api_router = APIRouter(
    prefix = "/indomarco-pizza",
    tags = ["indomarco_pizza"]
)

# Router
@api_router.get("/geom_kabkota_pizza", response_model=GeoJSONResponse)
def get_geom_kabkota_pizza():
    u_ip = di[IndomarcoPizzaUsecase]

    geom_kabkota_pizza_list = u_ip.get_geom_kabkota_pizza()
    response = GeoJSONResponse.from_db_model(
        name = "kabkota_pizza",
        crs = "CRS84",
        data = geom_kabkota_pizza_list
    )
    return response


@api_router.get("/geom_indonesia_kelurahan", response_model=GeoJSONResponse)
def get_geom_indonesia_kelurahan():
    u_ip = di[IndomarcoPizzaUsecase]

    geom_indonesia_kelurahan_list = u_ip.get_geom_indonesia_kelurahan()
    response = GeoJSONResponse.from_db_model(
        name = "indonesia_kelurahan",
        crs = "CRS84",
        data = geom_indonesia_kelurahan_list
    )
    return response
