from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()

# Load scraped data
with open("discourse_data.json", "r") as f:
    DATA = json.load(f)

class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None

@app.post("/api/")
async def answer(req: QuestionRequest):
    q = req.question.lower()
    # Simple search: find posts whose title or content matches
    matches = [d for d in DATA if q in d.get("title", "").lower() or q in d.get("content", "").lower()]
    if matches:
        top = matches[0]
        return {
            "answer": f"I found this post relevant: {top['title']}",
            "links": [
                {"url": top["url"], "text": top["title"]}
            ]
        }
    return {
        "answer": "Sorry, I couldn't find an answer in the TDS data.",
        "links": []
    }
