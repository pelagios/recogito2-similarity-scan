import unittest
from entities import Entities

class EntitiesTest(unittest.TestCase):

    def test_build_vector(self):
      docs = Entities.build_vector('rkprtr6jlhf2jv')
      self.assertEqual(1, 1)

if __name__ == '__main__':
  unittest.main()