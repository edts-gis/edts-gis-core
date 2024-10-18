import os
from typing import List

from src.helper.db import PostgreSQLHelper
from src.domain.convenience_brand_store import (
    BrandStore,
    Population
)


class ConvenienceBrandStoreRepositoryImpl:
    __db: PostgreSQLHelper
    __query_dir: str

    def __init__(self, db: PostgreSQLHelper):
        self.__db = db
        self.__query_dir = os.path.join(os.path.dirname(__file__), "query")


    # Public
    def count_brand_stores(self) -> int:
        cnt_brand_stores = int(
            self.__db.execute_query(
                self.__query_dir,
                "count_brand_stores.sql",
                params = {}
            )[0]["cnt"]
        )
        return cnt_brand_stores


    def get_brand_stores(self, page: int, limit: int) -> List[BrandStore]:
        offset = max(0, (page - 1)) * limit
        brand_stores = list(map(
            BrandStore.model_validate,
            self.__db.execute_query(
                self.__query_dir,
                "get_brand_stores.sql",
                params = {
                    "offset": offset,
                    "limit": limit
                }
            )
        ))
        return brand_stores


    def count_populations(self) -> int:
        cnt_populations = int(
            self.__db.execute_query(
                self.__query_dir,
                "count_populations.sql",
                params = {}
            )[0]["cnt"]
        )
        return cnt_populations


    def get_populations(self, page: int, limit: int) -> List[Population]:
        offset = max(0, (page - 1)) * limit
        populations = list(map(
            Population.model_validate,
            self.__db.execute_query(
                self.__query_dir,
                "get_populations.sql",
                params = {
                    "offset": offset,
                    "limit": limit
                }
            )
        ))
        return populations
