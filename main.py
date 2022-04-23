from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()
fake_db = []

class City(BaseModel):
    name :str
    timezone : str

@app.get("/")
def index():
    return {"hello":"world"}

@app.get("/cities")
def get_cities():
    results = []
    for city in fake_db:
        strs = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
        r = requests.get(strs)
        cur_time = r.json()["datetime"]
        results.append({"name":city["name"], "timezone":city["timezone"], "current_time":cur_time})

    return results

@app.get("/cities/{city_id}")
def get_city(city_id : int):
    city = fake_db[city_id-1]
    strs = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
    r = requests.get(strs)

    cur_time = r.json()["datetime"]

    return {"name":city["name"], "timezone":city["timezone"], "current_time":cur_time}

@app.post("/cities")
def create_city(city : City) :
    fake_db.append(city.dict())
    print(fake_db)
    return fake_db[-1]

@app.delete("/cities/{city_id}")
def delete_city(city_id : int):
    fake_db.pop(city_id-1)
    return {}