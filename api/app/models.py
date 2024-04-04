from pydantic import BaseModel

class PredictionRequest(BaseModel):
    opening_gross: float
    screens: float
    production_budget: float
    title_year: int
    aspect_ratio: float
    duration: int
    budget: float
    imbd_score: float

class PredictionResponse(BaseModel):
    worldwide_gross: float