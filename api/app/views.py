from .models import PredictionRequest
from .utils import get_model, transform_to_dataframe

model=get_model()

def get_prediction(request: PredictionRequest) -> float:
    data_to_predict = transform_to_dataframe(request)
    prediction = model.predict(data_to_predict)
    return max(0,prediction)