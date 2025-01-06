from fastapi import FastAPI
from api.routes import router
import uvicorn

app = FastAPI(
    title="Stock Market RAG System",
    description="A RAG-based system for stock market analysis and recommendations",
    version="1.0.0"
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
