from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.upload import router as upload_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(upload_router)

@app.get("/")
def health():
    return {"message": "dag ingestion running"}
