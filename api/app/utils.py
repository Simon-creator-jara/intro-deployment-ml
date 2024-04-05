from joblib import load
from sklearn.pipeline import Pipeline
from pydantic import BaseModel
from pandas import DataFrame
import os
from io import BytesIO
import pickle

def get_model() -> Pipeline:
    # model_path = os.environ.get('MODEL_PATH', 'model/model.pkl')
    #with open(model_path,'rb') as model_file:
        #model = load(BytesIO(model_file.read()))
    model=pickle.load(open("model/model.pkl", "rb"))
    return model

def transform_to_dataframe(class_model: BaseModel) -> DataFrame:
    transition_dictionary = {key:[value] for key, value in class_model.dict().items()}
    data_frame = DataFrame(transition_dictionary,columns=['opening_gross', 'screens', 'production_budget', 'title_year', 'aspect_ratio','duration', 'budget', 'imdb_score'])
    print(data_frame)
    return data_frame 
