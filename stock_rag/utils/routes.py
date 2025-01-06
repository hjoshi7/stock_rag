from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from core.advisor import StockAdvisor
from core.data_store import DataStore

router = APIRouter()
data_store = DataStore()
advisor = StockAdvisor(data_store.vector_store)

class Query(BaseModel):
    question: str
    context: Optional[dict] = None

class Response(BaseModel):
    answer: str
    sources: List[dict]

@router.post("/ask", response_model=Response)
async def ask_question(query: Query):
    try:
        answer = advisor.get_recommendation(query.question)
        sources = data_store.vector_store.similarity_search(query.question, k=3)
        return Response(
            answer=answer,
            sources=[{"title": s.metadata.get("title"), "source": s.metadata.get("source")} 
                    for s in sources]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
