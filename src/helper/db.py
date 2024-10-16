import os
from typing import List, Optional

from pydantic import SecretStr
from sqlalchemy import create_engine, text, Engine
from sqlalchemy.engine.url import URL



def get_db(db_uri: URL) -> Engine:
    engine = create_engine(
        db_uri,
        pool_pre_ping = True,
    )
    return engine


class PostgreSQLHelper:
    __db: Engine

    def __init__(self, db_uri: SecretStr):
        self.__db = get_db(db_uri)


    # Public
    def execute_query(self, query_dir: str, query_file: str, params: Optional[dict]) -> List[dict]:
        query_filepath = os.path.join(query_dir, query_file)
        with open(query_filepath, "r") as file:
            query = file.read()
        
        query_clause = text(query)
        with self.__db.connect() as conn:
            results_it = conn.execute(query_clause, params)
            results = [dict(row) for row in results_it.mappings().all()]
        
        return results
