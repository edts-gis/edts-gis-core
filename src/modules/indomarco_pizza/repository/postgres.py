import os
from typing import List

from src.helper.db import PostgreSQLHelper
from src.domain.indomarco_pizza import (
    GeomKabkotaPizza,
    GeomIndonesiaKelurahan
)


class IndomarcoPizzaPostgresRepositoryImpl:
    __db: PostgreSQLHelper
    __query_dir: str

    def __init__(self, db: PostgreSQLHelper):
        self.__db = db
        self.__query_dir = os.path.join(os.path.dirname(__file__), "query")


    # Public
    def get_geom_kabkota_pizza(self) -> List[GeomKabkotaPizza]:
        geom_kabkota_pizza_list = list(map(
            GeomKabkotaPizza.model_validate,
            self.__db.execute_query(
                self.__query_dir,
                "get_geom_kabkota_pizza.sql",
                params = {}
            )
        ))
        return geom_kabkota_pizza_list


    def get_geom_indonesia_kelurahan(self) -> List[GeomKabkotaPizza]:
        geom_indonesia_kelurahan_list = list(map(
            GeomIndonesiaKelurahan.model_validate,
            self.__db.execute_query(
                self.__query_dir,
                "get_geom_indonesia_kelurahan.sql",
                params = {}
            )
        ))
        return geom_indonesia_kelurahan_list
