import json
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.client import indices

# ////////////////////// DELETE ALL //////////////////////////////////////////
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
