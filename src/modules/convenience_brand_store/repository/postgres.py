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
    def get_brand_stores(self) -> List[BrandStore]:
        brand_stores = list(map(
            BrandStore.model_validate,
            self.__db.execute_query(
                self.__query_dir,
                "get_brand_stores.sql",
                params = {}
            )
        ))
        return brand_stores


    def get_populations(self) -> List[Population]:
        populations = list(map(
            Population.model_validate,
            self.__db.execute_query(
                self.__query_dir,
                "get_populations.sql",
                params = {}
            )
        ))
        return populations
