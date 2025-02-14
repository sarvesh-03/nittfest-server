"""
Main File
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.config.settings import settings
from server.routers import auth, questions, preferences
from server.config.database import engine, Base
from server.seed_data import seed

app = FastAPI()
app.include_router(auth.router)
app.include_router(questions.router)
app.include_router(preferences.router)


@app.on_event("startup")
async def startup():
    """
    Startup function
    """
    await seed()


origins = [settings.frontend_url]

Base.metadata.create_all(bind=engine)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/status")
def status():
    """
    get route for status
    """
    return {"status": "ok"}
