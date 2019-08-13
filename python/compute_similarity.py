from storage.documents import Documents
from similarity.metadata_similarity import MetadataSimilarity
import time

print("Fetching document metadata from DB")
docs = Documents.fetch_all()

start = time.time()
print(f"Computing similarity between {len(docs)} documents")
MetadataSimilarity.compute_pairwise(docs)

print(f"done - took {time.time() - start}")
