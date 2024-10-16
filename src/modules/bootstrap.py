from kink import di

from src.config import Config
from src.helper.db import PostgreSQLHelper

from src.domain import (
    convenience_brand_store,
    indomarco_pizza
)

from src.modules.convenience_brand_store.repository.postgres import ConvenienceBrandStoreRepositoryImpl
from src.modules.convenience_brand_store.usecase import ConvenienceBrandStoreUsecaseImpl

from src.modules.indomarco_pizza.repository.postgres import IndomarcoPizzaPostgresRepositoryImpl
from src.modules.indomarco_pizza.usecase import IndomarcoPizzaUsecaseImpl


# Repository
class Repository:
    indomarco_pizza_db_repo: indomarco_pizza.IndomarcoPizzaDBRepository
    convenience_brand_store_db_repo: convenience_brand_store.ConvenienceBrandStoreRepository

    def __init__(self, db: PostgreSQLHelper):
        self.indomarco_pizza_db_repo = IndomarcoPizzaPostgresRepositoryImpl(db)
        self.convenience_brand_store_db_repo = ConvenienceBrandStoreRepositoryImpl(db)


# Usecase
class Usecase:
    indomarco_pizza_usecase: indomarco_pizza.IndomarcoPizzaUsecase
    convenience_brand_store_usecase: convenience_brand_store.ConvenienceBrandStoreUsecase

    def __init__(self, r: Repository):
        self.indomarco_pizza_usecase = IndomarcoPizzaUsecaseImpl(r.indomarco_pizza_db_repo)
        self.convenience_brand_store_usecase = ConvenienceBrandStoreUsecaseImpl(r.convenience_brand_store_db_repo)


# Bootstrap
def bootstrap_di(C: Config):
    db = PostgreSQLHelper(C.DB_URI)

    r = Repository(db)
    u = Usecase(r)

    # Usecase
    di[indomarco_pizza.IndomarcoPizzaUsecase] = u.indomarco_pizza_usecase
    di[convenience_brand_store.ConvenienceBrandStoreUsecase] = u.convenience_brand_store_usecase
