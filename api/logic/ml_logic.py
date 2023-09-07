import torch
import pandas as pd
import os

def predict(df):
    model_save_name = 'xgb_optimized_classifier.pt'
    path = F"./{model_save_name}"
    optimal_xgb = torch.load(os.path.abspath(path))

    df = df.drop(['IsDefaulter','Payement_Value','Dues'],axis=1)
    df = df.iloc[: , 1:]

    prediction = optimal_xgb.predict_proba(df[1:5])[::,1]
    threshold = 0.5
    classified_predictions = (prediction >= threshold).astype(int)
    return classified_predictions