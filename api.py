from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="House Price API")
model = joblib.load('house_price_model.pkl')

class HouseFeatures(BaseModel):
    area: float
    bedrooms: int
    age: int
    proximity: float

@app.get("/")
def root():
    return {"message": "API chal raha hai!"}

@app.post("/predict")
def predict(features: HouseFeatures):
    input_data = np.array([[features.area, features.bedrooms, features.age, features.proximity]])
    pred = model.predict(input_data)[0]
    return {"predicted_price": round(float(pred), 2)}