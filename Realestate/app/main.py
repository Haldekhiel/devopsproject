from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class RealEstate(BaseModel):
    name: str
    amount: float
    expected_return: float
    risk_level: str

investments = {
    "stock": RealEstate(name="Stock", amount=1000.0, expected_return=0.1, risk_level="Medium"),
    "bond": RealEstate(name="Bond", amount=500.0, expected_return=0.05, risk_level="Low"),
    # ... other investment types
}

@app.get("/")
def read_root():
    return {"invetment": "connected"}

@app.get("/investments/")
def get_investments():
    return investments.values()

@app.get("/investments/{name}")
def get_investment(name: str):
    investment = investments.get(name)
    if investment is None:
        raise HTTPException(status_code=404, detail="Investment not found")
    return investment

@app.post("/investments/")
def create_investment(investment: RealEstate):
    investments[investment.name] = investment
    return {"message": "Investment created successfully"}


