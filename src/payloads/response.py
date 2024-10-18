import re
import copy
from typing import List, Union, Optional
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from pydantic import BaseModel
from pydantic_geojson import MultiPolygonModel, PolygonModel, PointModel



# Standard
class MessageResponse(BaseModel):
    message: str


# GeoJSON
class CRS(BaseModel):
    type: str
    properties: dict

class QGISFeatures(BaseModel):
    type: str
    properties: dict
    geometry: Union[MultiPolygonModel, PolygonModel, PointModel]

class GeoJSONResponse(BaseModel):
    type: str = "FeatureCollection"
    name: str
    crs: CRS
    features: List[QGISFeatures]

    @classmethod
    def from_db_model(
        cls,
        name: str,
        crs: str,
        data: List[BaseModel]
    ) -> "GeoJSONResponse":
        features = []
        for d in data:
            _d = d.model_dump()
            geometry = _d.pop("geometry")
            feature = QGISFeatures(
                type = "Feature",
                properties = _d,
                geometry = geometry
            )
            features.append(feature)

        return cls(
            name = name,
            crs = CRS(
                type = "name",
                properties = {
                    "name": f"urn:ogc:def:crs:OGC:1.3:{crs}"
                }
            ),
            features = features
        )


# Pagination
class PaginationURL(BaseModel):
    current: str
    prev: Optional[str] = None
    next: Optional[str] = None

    @classmethod
    def from_result(cls, current_url: str, page: int, total_page: int) -> "PaginationURL":
        parsed_url = list(urlparse(current_url))
        
        _prev = PaginationURL.__update_query(parsed_url, {"page": page - 1}) if (page > 1) else None
        _next = PaginationURL.__update_query(parsed_url, {"page": page + 1}) if (page < total_page) else None
        return cls(
            current = PaginationURL.__remove_domain(current_url),
            prev = PaginationURL.__remove_domain(_prev),
            next = PaginationURL.__remove_domain(_next)
        )

    @staticmethod
    def __update_query(parsed_url: list, update_value: dict) -> str:
        _parsed_url = copy.deepcopy(parsed_url)
        _query = dict(parse_qsl(_parsed_url[4]))
        
        _query.update(update_value)
        _parsed_url[4] = urlencode(_query)
        return urlunparse(_parsed_url)
    
    @staticmethod
    def __remove_domain(path: Optional[str]) -> Optional[str]:
        if path:
            return "/" + re.sub("^(http:|https:)\/\/", "", path).split("/", maxsplit=1)[-1]


class PaginateGeoJSONResponse(BaseModel):
    page: int
    page_size: int
    total_page: int
    total_data: int
    url: PaginationURL
    data: GeoJSONResponse

    @classmethod
    def from_result(
        cls,
        page: int,
        page_size: int,
        total_page: int,
        total_data: int,
        current_url: str,
        data: GeoJSONResponse,
    ) -> "PaginateGeoJSONResponse":

        return cls(
            page = page,
            page_size = page_size,
            total_page = total_page,
            total_data = total_data,
            url = PaginationURL.from_result(current_url, page, total_page),
            data = data
        )