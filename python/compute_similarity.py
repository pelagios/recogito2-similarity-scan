from storage.documents import Documents
from storage.entities import Entities
from similarity.entity_similarity import EntitySimilarity
from similarity.metadata_similarity import MetadataSimilarity
import time

print("Fetching document metadata from DB")
docs = Documents.fetch_all()

'''
start = time.time()
print(f"Computing similarity between {len(docs)} documents")
MetadataSimilarity.compute_pairwise(docs)

print(f"done - took {time.time() - start}")
'''

doc_ids = list(map(lambda doc: doc.id, docs))
print(f"Building vectors for {len(doc_ids)} documents (may take a while)")
vectors = list(map(lambda id: { 'document_id': id, 'uris': Entities.build_vector(id) }, doc_ids))
vectors = list(filter(lambda v: len(v['uris']) > 0, vectors))

print(f"Got {len(vectors)} non-empty vectors documents")
print("Computing pair-wise similarity")

EntitySimilarity.compute_pairwise(vectors)
