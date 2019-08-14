from storage.documents import Documents
from storage.entities import Entities
from storage.similarities import Similarities
from similarity.entity_similarity import EntitySimilarity
from similarity.metadata_similarity import MetadataSimilarity
import time

def compute_metadata_similarity(docs):
  start = time.time()
  print("Computing similarity between {0} documents".format(len(docs)))
  scores = MetadataSimilarity.compute_pairwise(docs)

  print("Writing results to DB")
  Similarities.store_metadata_similarity(scores)

  print("done - took {0}".format(time.time() - start))
  
def compute_entity_similarity(docs):
  start = time.time()
  doc_ids = list(map(lambda doc: doc.id, docs))
  print("Building vectors for {0} documents (may take a while)".format(len(doc_ids)))
  vectors = list(map(lambda id: { 'document_id': id, 'uris': Entities.build_vector(id) }, doc_ids))
  vectors = list(filter(lambda v: len(v['uris']) > 0, vectors))
  
  print("Got {0} non-empty vectors documents".format(len(vectors)))
  print("Computing pair-wise similarity")
  scores = EntitySimilarity.compute_pairwise(vectors)  

  print("Writing results to DB")
  Similarities.store_entity_similarity(scores)

  print("done - took {0}".format(time.time() - start))


print("Fetching document metadata from DB")
docs = Documents.fetch_all()
compute_metadata_similarity(docs)
compute_entity_similarity(docs)