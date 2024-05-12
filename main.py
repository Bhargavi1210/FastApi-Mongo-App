from fastapi import FastAPI
from collections.abc import MutableMapping  
from pymongo.mongo_client import MongoClient
from routes.route import router


app=FastAPI()

app.include_router(router)