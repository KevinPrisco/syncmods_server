from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import testRoute, modsRoute
from dotenv import load_dotenv

app = FastAPI()
app.include_router(testRoute.router)
app.include_router(modsRoute.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

load_dotenv()
