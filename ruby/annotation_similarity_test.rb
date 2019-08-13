require_relative 'annotation_similarity'
require 'test/unit'

'''
Test vectors

For A and B:
- Overlap is place 1 & 2 (weight 15)
- Union weight is 21
- Jaccard score 15 / 21 = 0.714

For B and C:
- Overlap is 2
- Union is 14
- Jaccard score 0.143
'''
VECTOR_A =   {
  document_id: 'document_a',
  uris: [
    [ "http://mygazetteer.org/place/1", 5 ],
    [ "http://mygazetteer.org/place/2", 2 ],
    [ "http://mygazetteer.org/place/3", 1 ],
    [ "http://mygazetteer.org/place/4", 1 ],
    [ "http://mygazetteer.org/place/5", 1 ]
  ]
}

VECTOR_B =   {
  document_id: 'document_b',
  uris: [
    [ "http://mygazetteer.org/place/1", 1 ],
    [ "http://mygazetteer.org/place/2", 7 ],
    [ "http://mygazetteer.org/place/6", 1 ],
    [ "http://mygazetteer.org/place/7", 1 ],
    [ "http://mygazetteer.org/place/8", 1 ]
  ]
}

VECTOR_C =   {
  document_id: 'document_b',
  uris: [
    [ "http://mygazetteer.org/place/1", 1 ],
    [ "http://mygazetteer.org/place/9", 2 ]
  ]
}

class TestSimilarity < Test::Unit::TestCase

  def test_first_example
    a_vs_b = Similarity.compute(VECTOR_A, VECTOR_B)
    assert_equal(a_vs_b, 15.0 / 21.0)
  end

  def test_second_example
    b_vs_c = Similarity.compute(VECTOR_B, VECTOR_C)
    assert_equal(b_vs_c, 2.0 / 14.0)
  end

end