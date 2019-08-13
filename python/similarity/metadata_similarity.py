import textdistance

class MetadataSimilarity:

  @staticmethod
  def compute_pairwise(documents):
    results = []

    for outer_idx, outer_doc in enumerate(documents):
      for inner_idx, inner_doc in enumerate(documents):

        if ((outer_idx < inner_idx) and 
            (outer_doc.owner != inner_doc.owner) and 
            (outer_doc.title != 'New document') and
            (inner_doc.title != 'New document') and
            (not outer_doc.title.lower().startswith('test')) and 
            (not inner_doc.title.lower().startswith('test'))):

          similarity = textdistance.jaro_winkler(outer_doc.title, inner_doc.title)
          if (similarity > 0.9):
            results.append({ 'doc_a': outer_doc, 'doc_b': inner_doc, 'score': similarity })

    return results
  
    