require 'pg'
require 'elasticsearch'
require 'json'

# Pull all document records from the DB
# conn = PG.connect('localhost', 5432, '', '', 'recogito-test', 'postgres', 'postgres')

# sql = 'SELECT author, title, owner, date_numeric FROM document'
# records = conn.exec(sql).select { |r| r['title'] != 'Welcome to Recogito' }

# Step 2: for each document, pull an aggregation from the index
#  - aggregate by URI
#  - get URI counts
#  - top 100 (?) places only
client = Elasticsearch::Client.new

response = client.search index: 'recogito', type: 'annotation', size: 0, body: { 
  query: { 
    bool: {
      must: [{
        term: { 
          'annotates.document_id': 'fb2f3hm1ihnwgn' 
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

puts JSON.pretty_generate(response)



