from fastapi import FastAPI

app = FastAPI(title="kyliescloset-bg")

@app.get("/health")
def health():
    return {"status": "ok"}