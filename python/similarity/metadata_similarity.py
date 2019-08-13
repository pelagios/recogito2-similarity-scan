import textdistance

class MetadataSimilarity:

  @staticmethod
  def compute_pairwise(documents):
    ctr = 0
    for outer_idx, outer_doc in enumerate(documents):
      for inner_idx, inner_doc in enumerate(documents):

        if ((outer_idx < inner_idx) and 
            (outer_doc.owner != inner_doc.owner) and 
            (outer_doc.title != 'New document') and
            (inner_doc.title != 'New document') and
            (not outer_doc.title.lower().startswith('test')) and 
            (not inner_doc.title.lower().startswith('test'))):

          ctr = ctr + 1 
          similarity = textdistance.jaro_winkler(outer_doc.title, inner_doc.title)
          if (similarity > 0.9):
            print(f"{outer_doc.title} ({outer_doc.owner}) - {inner_doc.title} ({inner_doc.owner}): {similarity}")

    print(f"Ran {ctr} comparisons")
  
    