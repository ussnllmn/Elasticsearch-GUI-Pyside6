import json
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.client import indices


# ////////////////////// UPDATE //////////////////////////////////////////
# es = Elasticsearch()
#
# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime.now(),
# }
# res = es.index(index="test-index222", id=1, document=doc)
# print(res['result'])

# res = es.get(index="test-index222", id=1)
# print(res['_source'])

# es.indices.refresh(index="test-index222")
#
# res = es.search(index="test-index222", query={"match_all": {}})
# print("Got %d Hits:" % res['hits']['total']['value'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
# client = Elasticsearch("http://localhost:9200")
# doc = {
#     'Title': 'author_name',
# }
# resp = client.update(index="test-covid", id='3nCTOH0BRcOD75nExr3G', body=doc)
# print(resp)
# print(resp['result'])
