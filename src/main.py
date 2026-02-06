from fastapi import FastAPI

app = FastAPI(title="Store API")

@app.get("/health")
def health():
    return {"status": "ok"}