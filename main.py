import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# read the environment (default dev.env)
ENV = os.getenv("APP_ENV", "dev")
load_dotenv(f"config/{ENV}.env")

# get the envvariable
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "")
origins = [origin.strip() for origin in ALLOWED_ORIGINS.split(",") if origin]

app = FastAPI(title="DeepHeart Backend")

# setting CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 範例 API
@app.get("/hello")
async def hello():
    return {"message": "Hello from FastAPI!"}

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI is running!"}