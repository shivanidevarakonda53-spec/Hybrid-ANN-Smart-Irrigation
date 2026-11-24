
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from prediction_service import predict_irrigation

app = FastAPI(title="Smart Irrigation AI Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://127.0.0.1:8080"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class ChatRequest(BaseModel):
    question: str

class PredictionRequest(BaseModel):
    features: dict

@app.get("/")
def home():
    return {"message": "Smart Irrigation AI Service is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        from rag_chatbot import ask_chatbot
        answer = ask_chatbot(request.question)
        return {"answer": answer}
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="Chatbot error: " + str(error)
        )

@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        result = predict_irrigation(request.features)
        return result
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed: " + str(error)
        )
