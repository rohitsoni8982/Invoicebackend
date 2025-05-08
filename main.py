from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from DataFile import databassconnection


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Product(BaseModel):
    name: str
    hsn: str
    taxable_value: str
    gst : str


class Add_Invoice(BaseModel):
    invoice_to_date: str
    invoice_from_date: str
    invoice_number: str
    billing_name: str
    billing_address: str
    billing_phone_number: str
    billing_gst_number: str
    items: List[Dict]

class Add_CreditNote(BaseModel):
    creadit_note_data : str
    credit_number : str
    billing_name : str
    billing_phone_number : str
    billing_address : str
    billing_gst_number : str
    invoice_number : str
    credit_amount : str
    description : str  
    invoice_date : str


@app.get("/your-endpoint")
async def your_get_method():
    return {"message": "This is a GET response"}

@app.post("/add_card")
def Add_Invoice(data: Dict[Any, Any]):
    data = dict(data)

    if not data.get("invoice_to_date"):
        return {"error": "invoice_to_date is required"}
    if not data.get("invoice_from_date"):
        return {"error": "invoice_from_date is required"}
    if not data.get("invoice_number"):
        return {"error": "invoice_number is required"}
    if not data.get("billing_name"):
        return {"error": "billing_name is required"}
    if not data.get("billing_address"):
        return {"error": "billing_address is required"}
    if not data.get("billing_phone_number"):
        return {"error": "billing_number is required"}
    if not data.get("billing_gst_number"):
        return {"error": "billing_gst_number is required"}
    if not data.items:
        return {"error": "items is required"}
    
    data = databassconnection.Invoice_data_store(data)

    return "successfully data stored"

@app.post("/credit_note")
def Add_CreditNote(data: Dict[Any, Any]):
    data = dict(data)

    if not data.get("creadit_note_data"):
        return {"error": "creadit_note_data is required"}
    if not data.get("credit_number"):
        return {"error": "credit_number is required"}
    if not data.get("invoice_number"):
        return {"error": "invoice_number is required"}
    if not data.get("billing_name"):
        return {"error": "billing_name is required"}
    if not data.get("billing_address"):
        return {"error": "billing_address is required"}
    if not data.get("billing_phone_number"):
        return {"error": "billing_number is required"}
    if not data.get("billing_gst_number"):
        return {"error": "billing_gst_number is required"}
    if not data.get("credit_amount"):
        return {"error": "credit_amount is required"}
    if not data.get("description"):
        return {"error": "description is required"}
    if not data.get("invoice_date"):
        return {"error": "invoice_date is required"}
    
    data = databassconnection.Credit_data_store(data)

    return "successfully data stored"

@app.post("/product")
def Product(data: Dict[Any, Any]):
    data = dict(data)
    
    if not data.get("name"):
        return {"error": "name is required"}
    if not data.get("hsn"):
        return {"error": "hsn is required"}
    if not data.get("gst"):
        return {"error": "gst is required"}
    
    data = databassconnection.product_data_store(data)
    
    return "successfully data stored"

@app.get("/last_invoice")
def last_invoice():
    data = databassconnection.get_next_invoice_number()
    return data

@app.get("/invoice_list")
def invoice_list():
    data = databassconnection.get_invoice_list()
    return data

@app.get("/product_list")
def product_list():
    data = databassconnection.get_product_list()
    return data   