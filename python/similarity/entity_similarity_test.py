import unittest
from entity_similarity import EntitySimilarity

VECTOR_A =   {
  'document_id': 'document_a',
  'uris': [
    [ 'http://mygazetteer.org/place/1', 5 ],
    [ 'http://mygazetteer.org/place/2', 2 ],
    [ 'http://mygazetteer.org/place/3', 1 ],
    [ 'http://mygazetteer.org/place/4', 1 ],
    [ 'http://mygazetteer.org/place/5', 1 ]
  ]
}

VECTOR_B =   {
  'document_id': 'document_b',
  'uris': [
    [ 'http://mygazetteer.org/place/1', 1 ],
    [ 'http://mygazetteer.org/place/2', 7 ],
    [ 'http://mygazetteer.org/place/6', 1 ],
    [ 'http://mygazetteer.org/place/7', 1 ],
    [ 'http://mygazetteer.org/place/8', 1 ]
  ]
}

class EntitieSimilarityTest(unittest.TestCase):

    def test_jaccard_similarity(self):
      similarity = EntitySimilarity.jaccard_similarity(VECTOR_A, VECTOR_B)
      self.assertEqual(similarity, 15.0 / 21.0)

if __name__ == '__main__':
  unittest.main()