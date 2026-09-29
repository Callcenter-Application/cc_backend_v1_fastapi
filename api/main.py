from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from api.seeders.seed import run_seeders
from api.routes.users import router as users
from api.routes.auth import router as auth
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    run_seeders()
    yield


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173/",
    "https://localhost:5173/",
    "http://127.0.0.1:5173",
    "https://127.0.0.1:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(users)
app.include_router(auth)




