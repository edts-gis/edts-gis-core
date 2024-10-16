from typing import List

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
    def get_brand_stores(self) -> List[BrandStore]:
        geom_brand_store_list = self.__db_repo.get_brand_stores()
        return geom_brand_store_list


    def get_populations(self) -> List[Population]:
        geom_population_list = self.__db_repo.get_populations()
        return geom_population_list
