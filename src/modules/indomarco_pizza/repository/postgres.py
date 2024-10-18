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
    def count_geom_kabkota_pizza(self) -> int:
        cnt_geom_kabkota_pizza = int(
            self.__db.execute_query(
                self.__query_dir,
                "count_geom_kabkota_pizza.sql",
                params = {}
            )[0]["cnt"]
        )
        return cnt_geom_kabkota_pizza


    def get_geom_kabkota_pizza(self, page: int, limit: int) -> List[GeomKabkotaPizza]:
        offset = max(0, (page - 1)) * limit
        geom_kabkota_pizza = list(map(
            GeomKabkotaPizza.model_validate,
            self.__db.execute_query(
                self.__query_dir,
                "get_geom_kabkota_pizza.sql",
                params = {
                    "offset": offset,
                    "limit": limit
                }
            )
        ))
        return geom_kabkota_pizza


    def count_geom_indonesia_kelurahan(self) -> int:
        cnt_geom_indonesia_kelurahan = int(
            self.__db.execute_query(
                self.__query_dir,
                "count_geom_indonesia_kelurahan.sql",
                params = {}
            )[0]["cnt"]
        )
        return cnt_geom_indonesia_kelurahan


    def get_geom_indonesia_kelurahan(self, page: int, limit: int) -> List[GeomKabkotaPizza]:
        offset = max(0, (page - 1)) * limit
        geom_indonesia_kelurahan = list(map(
            GeomIndonesiaKelurahan.model_validate,
            self.__db.execute_query(
                self.__query_dir,
                "get_geom_indonesia_kelurahan.sql",
                params = {
                    "offset": offset,
                    "limit": limit
                }
            )
        ))
        return geom_indonesia_kelurahan
