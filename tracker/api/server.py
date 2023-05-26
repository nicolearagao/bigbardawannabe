from fastapi import FastAPI

from tracker.db.session import engine, Base
from tracker.api.core import config 
from tracker.api.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

app.include_router(router, prefix=config.API_PREFIX)
