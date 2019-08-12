require 'pg'
require 'elasticsearch'
require 'json'

def fetch_documents() 
  conn = PG.connect('localhost', 5432, '', '', 'recogito-test', 'postgres', 'postgres')

  sql = 'SELECT id, title FROM document'
  records = conn.exec(sql).select { |r| r['title'] != 'Welcome to Recogito' }

  records.map { |row| row['id'] } # that's all we need
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
  Response format is as follows:

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
  buckets.map { |b| [ b['key'], b['doc_count'] ] }.to_h
end

client = Elasticsearch::Client.new
vectors = fetch_documents()
  .map { |id| { document_id: id, uris: build_vector(client, id) } }
  .select { |v| !v[:uris].empty? }

puts JSON.pretty_generate(vectors)







