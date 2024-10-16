SELECT
  ogc_fid,
  id,
  desa_seq,
  desa,
  density,
  kecamatan_seq,
  kecamatan,
  kabkota_seq,
  kabkota,
  provinsi_seq,
  provinsi,
  gid,
  area_ha,
  "population",
  jumlah_kk,
  jumlah_penduduk,
  elevation,
  ST_AsGeoJSON(ST_CollectionExtract("geometry"::geometry, 3)) AS "geometry"
FROM indomarco_pizza.geom_indonesia_kelurahan
WHERE TRUE
  AND provinsi IN (
    'JAWA BARAT',
    'BANTEN',
    'DKI JAKARTA'
  )
ORDER BY ogc_fid
OFFSET :offset
LIMIT :limit;
