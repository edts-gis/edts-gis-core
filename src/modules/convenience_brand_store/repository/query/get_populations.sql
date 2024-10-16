SELECT
  ogc_fid,
  "year",
  province,
  city,
  population_total,
  ST_AsGeoJSON("geometry") AS "geometry"
FROM convenience_brand_store.populations
WHERE TRUE;
