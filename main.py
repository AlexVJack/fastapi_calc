from fastapi import FastAPI
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["calcdb"]

app = FastAPI()


@app.get("/add/{a}/{b}")
async def add_operation(a: float, b: float):
    c = a + b
    mydb.results.insert_one({"operation": f"{a} + {b}", "result": c})
    return {"result of addition": c}


@app.get("/sub/{a}/{b}")
async def sub_operation(a: float, b: float):
    c = a - b
    mydb.results.insert_one({"operation": f"{a} - {b}", "result": c})
    return {"result of subtraction": c}


@app.get("/div/{a}/{b}")
async def div_operation(a: float, b: float):
    if b == 0:
        return "Unfortunately, Your rude Earth technology \
        does not allow dividing by zero!"
    c = a / b
    mydb.results.insert_one({"operation": f"{a} / {b}", "result": c})
    return {"result of division": c}


@app.get("/mult/{a}/{b}")
async def mult_operation(a: float, b: float):
    c = a * b
    mydb.results.insert_one({"operation": f"{a} * {b}", "result": c})
    return {"result of multiplication": c}
