SELECT
  ogc_fid,
  store_company,
  store_name,
  province,
  city,
  subdistrict,
  ST_AsGeoJSON("geometry") AS "geometry"
FROM convenience_brand_store.brand_stores
WHERE TRUE;
