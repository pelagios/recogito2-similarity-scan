require 'pg'
require 'elasticsearch'
require 'json'

def fetch_documents() 
  conn = PG.connect('localhost', 5432, '', '', 'recogito-test', 'postgres', 'postgres')

  sql = 'SELECT id, title FROM document'
  conn.exec(sql).select { |r| r['title'] != 'Welcome to Recogito' }
end

def build_vector(client, document_id)
  response = client.search index: 'recogito', type: 'annotation', size: 0, body: { 
    query: { 
      bool: {
        must: [{
          term: { 
            'annotates.document_id': document_id 
          }
        },{
          nested: {
            path: 'bodies',
            query: {
              term: { 'bodies.type': 'PLACE' }
            }
          }
        }]
      }
    },
    aggregations: {
      bodies: {
        nested: {
          path: 'bodies'
        },
        aggregations: {
          uris: {
            terms: { field: 'bodies.reference.uri' }
          }
        }
      }
    }
  }

  '''
  ElasticSearch response format is as follows (relevant bits only):
  {
    ...
    aggregations: {
      bodies: {
        doc_count: ...
        uris: {
          ...
          buckets: [
            { key:..., doc_count: ...}
          ]
        }
      }
    }
  }
  '''

  buckets = response['aggregations']['bodies']['uris']['buckets']
  buckets.map { |b| [ b['key'], b['doc_count'] ] }
end

'''
Each element is a "document descriptor" in the form

{
  document_id: ...,
  uris: [
    [ "http://mygazetteer.org/place/12345": 5 ],
    ...
  }
}

Compare for Jaccard-type similarity (num of intersection vs. num of union)
'''
class Similarity

  def self.compute(a, b)
    values_a = a[:uris]
    values_b = b[:uris]

    count_a = values_a.reduce(0) { |sum, tuple| sum + tuple[1] }
    count_b = values_b.reduce(0) { |sum, tuple| sum + tuple[1] }

    intersection = values_a.reduce(0) do |sum, tuple_a| 
      tuple_b = values_b.detect { |t| t[0] == tuple_a[0] }

      if tuple_b.nil?
        sum
      else
        sum + tuple_a[1] + tuple_b[1]
      end
    end

    intersection.to_f / (count_a + count_b)
  end

end

if __FILE__==$0
  # this will only run if the script was the main, not load'd or require'd
  '''
  Fetch all document IDs from the DB
  '''
  documents = fetch_documents()
  document_ids = documents.map { |row| row['id'] } # that's all we need

  puts "Building vectors for #{document_ids.size} documents (may take a while)"

  client = Elasticsearch::Client.new
  vectors = document_ids
    .map { |id| { document_id: id, uris: build_vector(client, id) } }
    .select { |v| !v[:uris].empty? }

  puts "Got #{vectors.size} non-empty vectors documents"
  # puts JSON.pretty_generate(vectors)

  puts "Computing pair-wise similarity"

  vectors.each_with_index do |outer, outer_idx|
    # TODO this will compute every pair twice... optimize
    vectors.each_with_index do |inner, inner_idx|
      if outer_idx < inner_idx
        similarity = Similarity.compute(outer, inner)

        if (similarity > 0.9)
          doc_a = documents.detect { |row| row['id'] == outer[:document_id] }
          doc_b = documents.detect { |row| row['id'] == inner[:document_id] }

          puts "#{doc_a['title']} - #{doc_b['title']}: #{similarity}"
        end
      end
    end
  end

  puts "Done."
end