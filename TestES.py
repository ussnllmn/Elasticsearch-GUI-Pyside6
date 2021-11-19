import json
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.client import indices
# create a new instance of the Elasticsearch client class

# elastic = Elasticsearch()
#
# # get the names of the indexes
# all_indices = elastic.indices.get_alias().keys()
# print ("\nAttempting to delete", len(all_indices), "indexes.")
#
# # iterate the list of indexes
# for _index in all_indices:
# # attempt to delete ALL indices in a 'try' and 'catch block
#     try:
#         if "." not in _index: # avoid deleting indexes like `.kibana`
#             elastic.indices.delete(index=_index)
#             print ("Successfully deleted:", _index)
#     except Exception as error:
#         print ('indices.delete error:', error, 'for index:', _index)
#
# # now create a new index
# elastic.indices.create(index="new-index")
#
# # verify the new index was created
# final_indices = elastic.indices.get_alias().keys()
# print ("\nNew total:", len(final_indices), "indexes.")
# for _index in final_indices:
#     print ("Index name:", _index)

es = Elasticsearch()
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


# ///////////////////////////////////////////////////////////////////////
# print(es.cluster.health())
# print(es.indices.get_alias("*"))

# res = es.delete(index="test-index", id=1)
# print(res['result'])

# es.delete(index="test-index", id=1)

res = es.indices.create(index='test-covid')
print(res)
#
# res = es.indices.delete(index='some-new-index')
# print(res)


# es.indices.delete(index='test-index', ignore=[400, 404])
# for index in es.indices.get('*'):
#   print(index)
# ///////////////////////////////////////////////////////////////////////