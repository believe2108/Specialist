from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def main() -> dict[str, str]:
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    uvicorn.run("HelloWord:app", port=8000, reload=True)
