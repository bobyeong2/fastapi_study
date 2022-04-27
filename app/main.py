from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import items, users, endpoint
from app.database import database, models
from app.library.helpers import *

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)
app.mount("/root/01_study/static", StaticFiles(directory="/root/01_study/static"), name="static")

app.include_router(users.router)
app.include_router(items.router)
app.include_router(endpoint.router)