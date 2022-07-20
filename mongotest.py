import pymongo
client = pymongo.MongoClient("mongodb+srv://rishabh:rish850587582@cluster0.5zi5qky.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"rishabh",
    "surname":"mankar",
    "email":"rish@gmail.com"
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)

