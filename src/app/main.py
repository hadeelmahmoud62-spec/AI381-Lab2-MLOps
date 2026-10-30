from pathlib import Path
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "model.joblib"

FEATURES = [
    "tenure_months",
    "monthly_fee",
    "contract",
    "internet_service",
    "support_calls",
]


class Customer(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tenure_months: int = Field(ge=0)
    monthly_fee: float = Field(ge=0)
    contract: str
    internet_service: str
    support_calls: int = Field(ge=0)


app = FastAPI(title="AI381 Lab 2 Churn API")

model = joblib.load(MODEL_PATH)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(customer: Customer):
    data = customer.model_dump()
    X = pd.DataFrame([data], columns=FEATURES)
    probability = float(model.predict_proba(X)[0, 1])

    return {"churn_probability": round(probability, 3)}