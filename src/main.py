from fastapi import FastAPI
from src.presentation.routes.router import router


app = FastAPI(title="Store API")
app.include_router(router)

#@app.get("/health")
#def health():
#    return {"status": "ok"}

