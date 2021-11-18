# import the elasticsearch client library
from elasticsearch import Elasticsearch

# import the exceptions library for Elasticsearch
from elasticsearch import exceptions

# import Python's json library to format JSON responses
import json
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.client import indices

es = Elasticsearch()

# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime.now(),
# }
# res = es.index(index="test-index", id=1, document=doc)
# print(res['result'])

# res = es.get(index="test-index", id=1)
# print(res['_source'])

# es.indices.refresh(index="test-index")

# res = es.search(index="test-index", query={"match_all": {}})
# print("Got %d Hits:" % res['hits']['total']['value'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

# print(es.cluster.health())
# print(es.indices.get_alias("*"))

es.indices.delete(index='test-index', ignore=[400, 404])
# for index in es.indices.get('*'):
#   print(index)