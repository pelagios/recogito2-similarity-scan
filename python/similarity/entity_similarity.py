from functools import reduce

class EntitySimilarity:

  @staticmethod
  def jaccard_similarity(a, b):
    values_a = a['uris']
    values_b = b['uris']

    count_a = reduce((lambda sum, tuple: sum + tuple[1]), values_a, 0)
    count_b = reduce((lambda sum, tuple: sum + tuple[1]), values_b, 0)

    def intersect(sum, tuple_a):
      tuple_b = next((t for t in values_b if t[0] == tuple_a[0]), None)
      if tuple_b is None:
        return sum
      else:
        return sum + tuple_a[1] + tuple_b[1]

    intersection = reduce(intersect, values_a, 0)

    return intersection / (count_a + count_b)

  @staticmethod
  def compute_pairwise(vectors):
    results = []

    for outer_idx, outer_vec in enumerate(vectors):
      for inner_idx, inner_vec in enumerate(vectors): 
        if (outer_idx < inner_idx):
          similarity = EntitySimilarity.jaccard_similarity(outer_vec, inner_vec)
          if (similarity > 0.9):
            results.append({ 'vec_a': outer_vec, 'vec_b': inner_vec, 'score': similarity })

    return results