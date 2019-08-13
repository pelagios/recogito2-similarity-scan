import unittest
from metadata_similarity import MetadataSimilarity

class MetadataSimilarityTest(unittest.TestCase):

  def test_compute(self):
    distance = MetadataSimilarity.compute('martha', 'marhta')
    self.assertEqual(distance, 0.96)

if __name__ == '__main__':
  unittest.main()