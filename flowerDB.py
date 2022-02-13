import pymongo
from itertools import count
import datetime

client = pymongo.MongoClient("mongodb+srv://12345:12345@cluster0.htukn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.FlowersDB
coll = db.orders
coll2 = db.products



# #создание нов перемен в колекц orders
# data = [
# 	{
#       "amount" : 1,
#       "_id" : "-MiYEZuzULM-wg0KuKPw",
#       "name" : "White roses",
#       "price" : 3.5
# 	},
# 	{
#       "amount" : 1,
#       "_id" : "-MiYEWhO5qzS_hndN60b",
#       "name" : "Aquilégia bush",
#       "price" : 10.5
# 	},
# 	{
#       "amount" : 1,
#       "_id" : "-Mir-fwGo-IcTn3oTOEo",
#       "name" : "Bouquet of tulips",
#       "price" : 7.5
# 	}
# ]
# coll.insert_many(data)
# print("Данні записані!")#если дан запишутся в бд, выведет это сообщение


def add_new_order():
      arr = []
      for value in coll.insert_one({"amount" : 1, "_id" : "test1", "name" : "White roses", "price" : 3.5}):
            arr.append(value)
            print(value)
	return arr





# #создание нов перемен в колекц products
# data = [
# 	{	
# 		"_id" : "-MiYEZuzULM-wg0KuKPw",
#       "description" : "Tears of Falka",
#       "eng_name" : "White roses",
#       "id" : "m1",
#       "img" : "no_img(should be a link)",
#       "location" : "elven forest",
#       "name" : "elven flower field",
#       "price" : 3.5,
#       "weight" : 50
#    },
# 	{
# 		"_id" : "-MiYEWhO5qzS_hndN60b",
#       "description" : "Lafael",
#       "eng_name" : "Aquilégia bush",
#       "id" : "m2",
#       "img" : "no_img(should be a link)",
#       "location" : "elven forest",
#       "name" : "elven flower field",
#       "price" : 10.5,
#       "weight" : 25
#    },
# 	{
# 		"_id" : "-Mir-fwGo-IcTn3oTOEo",
#       "description" : "hacca",
#       "eng_name" : "Bouquet of tulips",
#       "id" : "m2",
#       "img" : "no_img(should be a link)",
#       "location" : "elven forest",
#       "name" : "elven flower field",
#       "price" : 7.5,
#       "weight" : 25
#    },
# ]
# coll.insert_many(data)
# print("Данні записані!")

def get_products():
	arr = []
	for value in coll2.find():
		arr.append(value)
		print(value)
	return arr

# #удаление всех елементов из колекции
# res = coll.delete_many({})
# print("deleted:", res.deleted_count)