CREATE TABLE similarity (
  doc_id_a TEXT NOT NULL,
  doc_id_b TEXT NOT NULL,
  title_jaro_winkler DOUBLE PRECISION DEFAULT 0,
  entity_jaccard DOUBLE PRECISION DEFAULT 0,
  PRIMARY KEY (doc_id_a, doc_id_b)
);