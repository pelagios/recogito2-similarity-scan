from elasticsearch import Elasticsearch

class Entities:

  @staticmethod
  def build_vector(document_id):
    es = Elasticsearch()

    response = es.search(index='recogito', doc_type='annotation', params={ 'size': 0 }, body={ 
      'query': { 
        'bool': {
          'must': [{
            'term': { 
              'annotates.document_id': document_id
            }
          },{
            'nested': {
              'path': 'bodies',
              'query': {
                'term': { 'bodies.type': 'PLACE' }
              }
            }
          }]
        }
      },
      'aggregations': {
        'bodies': {
          'nested': {
            'path': 'bodies'
          },
          'aggregations': {
            'uris': {
              'terms': { 'field': 'bodies.reference.uri' }
            }
          }
        }
      }
    })

    print(response)
    return