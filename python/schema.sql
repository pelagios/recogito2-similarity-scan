CREATE TABLE similarity (
  doc_id_a TEXT NOT NULL,
  doc_id_b TEXT NOT NULL,
  title_jaro_winkler DOUBLE PRECISION,
  entity_jaccard DOUBLE PRECISION,
  PRIMARY KEY (doc_id_a, doc_id_b)
);