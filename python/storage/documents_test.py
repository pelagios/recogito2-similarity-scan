import unittest
from documents import Documents

class DocumentsTest(unittest.TestCase):

    def test_fetch_all(self):
      docs = Documents.fetch_all()
      self.assertEqual(len(docs), 4052)

if __name__ == '__main__':
  unittest.main()