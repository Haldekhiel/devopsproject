from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#test
app = FastAPI()

class RealEstate(BaseModel):
    id: int
    title: str
    price: float
    area: float 
    property_type: str 
    latitude: float
    longitude: float

real_estates = {
    1: RealEstate(id=1, title="Spacious Villa in Al-Malqa", price=3500000, area=380, property_type="Residential",latitude=24.6789, longitude=46.6543),
    2: RealEstate(id=2, title="Commercial Building in Olaya", price=3000000, area=520, property_type="Commercial",latitude=24.7123, longitude=46.7890),
    3: RealEstate(id=3, title="Agricultural Land in Wadi Hanifah", price=800000, area=2000, property_type="Agricultural",latitude=24.5678, longitude=46.4321),
}

@app.get("/real_estates/")  
def get_real_estates():
    return list(real_estates.values())

@app.get("/real_estates/{real_estate_id}")  
def get_real_estate(real_estate_id: int):
    real_estate = real_estates.get(real_estate_id)
    if real_estate is None:
        raise HTTPException(status_code=404, detail="Real estate not found")
    return real_estate

@app.post("/real_estates/")  
def create_real_estate(real_estate: RealEstate):
    new_id = max(real_estates.keys()) + 1
    real_estate.id = new_id
    real_estates[new_id] = real_estate
    return {"id": new_id}
