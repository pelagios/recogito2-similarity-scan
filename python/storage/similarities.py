from storage.db import DB
from sqlalchemy import create_engine

class Similarities:

  @staticmethod
  def store_metadata_similarity(scores):
    db = create_engine(DB.get_db_string())

    for s in scores:
      a = s['doc_a']['id']
      b = s['doc_b']['id']
      score = s['score']
      db.execute("""INSERT INTO similarity 
        (doc_id_a, doc_id_b, title_jaro_winkler) 
      VALUES ('{0}', '{1}', {2})
      ON CONFLICT(doc_id_a, doc_id_b) DO UPDATE
        SET title_jaro_winkler = {3}""".format(a, b, score, score))

  @staticmethod
  def store_entity_similarity(scores):
    db = create_engine(DB.get_db_string())

    for s in scores:
      a = s['vec_a']['document_id']
      b = s['vec_b']['document_id']
      score = s['score']
      db.execute("""INSERT INTO similarity 
        (doc_id_a, doc_id_b, entity_jaccard) 
      VALUES ('{0}', '{1}', {2})
      ON CONFLICT(doc_id_a, doc_id_b) DO UPDATE
        SET entity_jaccard = {3}""".format(a, b, score, score))