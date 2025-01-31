import unittest
from entities import Entities

class EntitiesTest(unittest.TestCase):

    def test_build_vector(self):
      docs = Entities.build_vector('rkprtr6jlhf2jv')
      self.assertEqual(len(docs), 10)

if __name__ == '__main__':
  unittest.main()