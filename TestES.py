import json
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.client import indices
es = Elasticsearch()

res = es.get(index="test-covid", id=1)
print(res['_source'])