from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.upload import router as upload_router
from app.api.retrieve import router as retrieve_router
from app.api.chat import router as chat_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(upload_router)
app.include_router(retrieve_router)
app.include_router(chat_router)

@app.get("/")
def health():
    
    return {"message": "dag ingestion running"}
