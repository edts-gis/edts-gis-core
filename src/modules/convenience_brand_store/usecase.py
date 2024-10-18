from typing import List, Tuple

from src.domain.convenience_brand_store import (
    BrandStore,
    Population,
    ConvenienceBrandStoreRepository,
)


class ConvenienceBrandStoreUsecaseImpl:
    __db_repo: ConvenienceBrandStoreRepository

    def __init__(self, db_repo: ConvenienceBrandStoreRepository):
        self.__db_repo = db_repo


    # Public
    def get_brand_stores(self, page: int, limit: int) -> Tuple[int, List[BrandStore]]:
        count_brand_store = self.__db_repo.count_brand_stores()
        brand_stores = self.__db_repo.get_brand_stores(page, limit)
        return (count_brand_store, brand_stores)


    def get_populations(self, page: int, limit: int) -> Tuple[int, List[Population]]:
        count_population = self.__db_repo.count_populations()
        populations = self.__db_repo.get_populations(page, limit)
        return (count_population, populations)
