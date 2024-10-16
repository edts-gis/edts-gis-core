from typing import List

from src.domain.indomarco_pizza import (
    GeomKabkotaPizza,
    GeomIndonesiaKelurahan,
    IndomarcoPizzaDBRepository
)


class IndomarcoPizzaUsecaseImpl:
    __db_repo: IndomarcoPizzaDBRepository

    def __init__(self, db_repo: IndomarcoPizzaDBRepository):
        self.__db_repo = db_repo


    # Public    
    def get_geom_kabkota_pizza(self) -> List[GeomKabkotaPizza]:
        geom_kabkota_pizza_list = self.__db_repo.get_geom_kabkota_pizza()
        return geom_kabkota_pizza_list


    def get_geom_indonesia_kelurahan(self) -> List[GeomIndonesiaKelurahan]:
        geom_indonesia_kelurahan_list = self.__db_repo.get_geom_indonesia_kelurahan()
        return geom_indonesia_kelurahan_list
