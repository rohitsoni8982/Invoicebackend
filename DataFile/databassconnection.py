from bson.json_util import dumps
from bson import json_util
import json
from pymongo import MongoClient
from pymongo import DESCENDING
from datetime import datetime
import re

def connect():
    uspass = 'rohit8982'
    connect = f"mongodb+srv://rohit8982:{uspass}@cluster0.lyn00.mongodb.net/"
    client = MongoClient(connect , serverSelectionTimeoutMS=5000)
    print("Connected to MongoDB")
    db = client['MG']  # Replace with your database name
    return db

def Invoice_data_store(add_card_data):
    db = connect()
    # check is vehicle already registred or not
    collection = db['invoice']
    collection.insert_one(add_card_data)
    print(add_card_data)
    return ''

# def get_invoice_number():
#     db = connect()
#     collection = db['invoice']  # using your actual collection

#     current_year = str(datetime.now().year)
#     prefix = f"MG/{current_year}/"

#     # Get the latest invoice sorted by invoice_number
#     latest_invoice = collection.find({"invoice_number": {"$regex": f"^MG/{current_year}/"}}).sort("invoice_number", DESCENDING).limit(1)
#     latest_invoice_list = list(latest_invoice)

#     if latest_invoice_list:
#         last_invoice_number = latest_invoice_list[0].get("invoice_number", "")
#         match = re.search(rf"MG/{current_year}/(\d+)", last_invoice_number)

#         if match:
#             last_number = int(match.group(1)) + 1
#             next_invoice = f"{prefix}{str(last_number).zfill(6)}"
#         else:
#             next_invoice = f"{prefix}000001"
#     else:
#         next_invoice = f"{prefix}000001"

#     return {"invoice_number": next_invoice}

def get_next_invoice_number():
    db = connect()
    collection = db['invoice']  # Replace with your actual collection

    current_year = str(datetime.now().year)
    prefix = f"MG/{current_year}/"

    # Get the latest invoice sorted by invoice_number
    latest_invoice = collection.find({"invoice_number": {"$regex": f"^MG/{current_year}/"}}).sort("invoice_number", DESCENDING).limit(1)
    latest_invoice_list = list(latest_invoice)

    if latest_invoice_list:
        last_invoice_number = latest_invoice_list[0].get("invoice_number", "")
        match = re.search(rf"MG/{current_year}/(\d+)", last_invoice_number)

        if match:
            last_number = int(match.group(1)) + 1
            next_invoice = f"{prefix}{str(last_number).zfill(6)}"
        else:
            next_invoice = f"{prefix}000001"
    else:
        next_invoice = f"{prefix}000001"

    return {"invoice_number": next_invoice}
    # return {"last_invoice_number": last_invoice_number,"invoice_number": next_invoice}

def convert_objectid(data):
    if isinstance(data, list):
        for item in data:
            item['_id'] = str(item['_id'])
    else:
        data['_id'] = str(data['_id'])
    return data

def get_invoice_list():
    db = connect()

    collection = db['invoice']
    data = list(collection.find())

    return convert_objectid(data)

def product_data_store(product_data):
    db = connect()
    collection = db['product']
    collection.insert_one(product_data)
    print(product_data)
    return ''

def get_product_list():
    db = connect()
    collection = db['product']
    data = list(collection.find())
    return convert_objectid(data)

