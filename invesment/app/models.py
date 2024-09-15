from pydantic import BaseModel

class Investment(BaseModel):
    name: str
    amount: float
    expected_return: float
    risk_level: str
