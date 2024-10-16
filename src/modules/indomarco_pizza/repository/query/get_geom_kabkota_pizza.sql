SELECT
  ogc_fid,
  pt_id,
  seg_id,
  ring_id,
  ST_AsGeoJSON("geometry") AS "geometry"
FROM indomarco_pizza.geom_kabkota_pizza
WHERE TRUE
  AND pt_id IN ('100', '101', '102', '103', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99');
