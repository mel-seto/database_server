from fastapi import FastAPI, Request, HTTPException
import uvicorn

app = FastAPI()

# In-memory key-value store
store = {}
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/set")
async def set_key_value(request: Request):
    query_params = dict(request.query_params)

    if not query_params:
        raise HTTPException(status_code=400, detail="No query parameters provided.")

    key, value = next(iter(query_params.items()))
    store[key] = value
    return {"message": "Stored successfully", "key": key, "value": value }

@app.get("/get")
async def get_value(key: str):
    if key not in store:
        raise HTTPException(status_code=404, detail=f"Key '{key}' not found")

    return {"key": key, "value": store[key]}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=4000, reload=True)