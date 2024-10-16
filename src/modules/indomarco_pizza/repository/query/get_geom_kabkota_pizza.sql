SELECT
  ogc_fid,
  pt_id,
  seg_id,
  ring_id,
  ST_AsGeoJSON("geometry") AS "geometry"
FROM indomarco_pizza.geom_kabkota_pizza
WHERE TRUE;
