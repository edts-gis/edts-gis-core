from fastapi import FastAPI

from src.routers import (
    convenience_brand_store,
    indomarco_pizza,
)


def configure_routers(app: FastAPI):
    app.include_router(convenience_brand_store.api_router)
    app.include_router(indomarco_pizza.api_router)

