import json
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.client import indices
es = Elasticsearch()

resp = es.search(index="test-covid", query={"match_all": {}})
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print("%(Title)s %(Content)s" % hit["_source"])