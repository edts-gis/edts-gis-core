from typing import List, Union

from pydantic import BaseModel
from pydantic_geojson import MultiPolygonModel, PolygonModel, PointModel


class MessageResponse(BaseModel):
    message: str

# QGIS GeoJSON
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
    def from_db_dict(
        cls,
        name: str,
        crs: str,
        data: List[dict]
    ) -> "GeoJSONResponse":
        features = []
        for d in data:
            geometry = d.pop("geometry")
            feature = QGISFeatures(
                type = "Feature",
                properties = d,
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
