import pymongo

#Establish a connection to our database
client = pymongo.MongoClient("mongodb://localhost:27017")

#create or select a database
mydb = client["lexicondb"]

#Create or select a collection in the db
mycol = mydb["customrts"]

customer_data = {
    "name": "Diana",
    "email": "diana@email.com",
    "age": 20
}
#insert one document into the collection
result = mycol.insert_one(customer_data)
print("Inserted document ID", result.inserted_id)

#prints all documents in the collection in the terminal directly
print("All documents in the collection:")
for document in mycol.find():
    print(document)


#update a document

query = {"name": "Cammelia"}
new_value = {"$set":{"age": 34}}
mycol.update_one(query, new_value)
print("Document updated")

print("(AFTER THE UPDATE) All documents in the collection:")
for document in mycol.find():
    print(document)

#delete a document
delete_query = {"name": "Diana"}
#if to delete multiple, use delete_many
mycol.delete_many(delete_query)
print("Document deleted")
for document in mycol.find():
    print(document)