from typing import List, Tuple

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
    def get_geom_kabkota_pizza(self, page: int, limit: int) -> Tuple[int, List[GeomKabkotaPizza]]:
        count_geom_kabkota_pizza = self.__db_repo.count_geom_kabkota_pizza()
        geom_kabkota_pizza = self.__db_repo.get_geom_kabkota_pizza(page, limit)
        return (count_geom_kabkota_pizza, geom_kabkota_pizza)


    def get_geom_indonesia_kelurahan(self, page: int, limit: int) -> List[GeomIndonesiaKelurahan]:
        count_geom_kabkota_pizza = self.__db_repo.count_geom_indonesia_kelurahan()
        geom_indonesia_kelurahan = self.__db_repo.get_geom_indonesia_kelurahan(page, limit)
        return (count_geom_kabkota_pizza, geom_indonesia_kelurahan)
