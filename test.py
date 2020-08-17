import pymongo
import pprint


client = pymongo.MongoClient(
            "mongodb+srv://AlexUA:IIDS520a@alexua-claster.eulvj.gcp.mongodb.net/<AlexUA-Claster>?retryWrites=true&w=majority")
db = client.base_avto
post = {"avto": "1",
   "qw": "w"
   }

list_avto = db.list_avto
#avto = list_avto.insert_one(post).inserted_id
#print(avto)

pprint.pprint(list_avto.find_one({'rt':'1235'}))
