from pymongo import MongoClient
client=MongoClient("mongodb+srv://bhargavivaidya:bhargavi3333@cluster0.pjcebbj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


db=client.posts_db

collection_name=db["posts_collection"]