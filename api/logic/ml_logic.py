import torch
import pandas as pd
import os
import numpy as np

from imblearn.over_sampling import SMOTE

def clean_data(df):

    df['IsDefaulter'] = df['default.payment.next.month']
    df.drop('default.payment.next.month', axis=1)
    fil = (df['EDUCATION'] == 5) | (df['EDUCATION'] == 6) | (df['EDUCATION'] == 0)
    df.loc[fil, 'EDUCATION'] = 4
    fil = df['MARRIAGE'] == 0
    df.loc[fil, 'MARRIAGE'] = 3

    categorical_features = ['SEX', 'EDUCATION', 'MARRIAGE']
    df_cat = df[categorical_features]
    df_cat['Defaulter'] = df['IsDefaulter']
    df_cat.replace({'SEX': {1 : 'MALE', 2 : 'FEMALE'}, 'EDUCATION' : {1 : 'graduate school', 2 : 'university', 3 : 'high school', 4 : 'others'}, 'MARRIAGE' : {1 : 'married', 2 : 'single', 3 : 'others'}}, inplace = True)

    df.rename(columns={'PAY_0':'PAY_SEPT','PAY_2':'PAY_AUG','PAY_3':'PAY_JUL','PAY_4':'PAY_JUN','PAY_5':'PAY_MAY','PAY_6':'PAY_APR'},inplace=True)
    df.rename(columns={'BILL_AMT1':'BILL_AMT_SEPT','BILL_AMT2':'BILL_AMT_AUG','BILL_AMT3':'BILL_AMT_JUL','BILL_AMT4':'BILL_AMT_JUN','BILL_AMT5':'BILL_AMT_MAY','BILL_AMT6':'BILL_AMT_APR'}, inplace = True)
    df.rename(columns={'PAY_AMT1':'PAY_AMT_SEPT','PAY_AMT2':'PAY_AMT_AUG','PAY_AMT3':'PAY_AMT_JUL','PAY_AMT4':'PAY_AMT_JUN','PAY_AMT5':'PAY_AMT_MAY','PAY_AMT6':'PAY_AMT_APR'},inplace=True)

    df['AGE']=df['AGE'].astype('int')
    df = df.astype('int')

    smote = SMOTE()

    # fit predictor and target variable
    x_smote, y_smote = smote.fit_resample(df.iloc[:,0:-1], df['IsDefaulter'])

    columns = list(df.columns)
    columns.pop()
    balance_df = pd.DataFrame(x_smote, columns=columns)
    balance_df['IsDefaulter'] = y_smote

    df_fr = balance_df.copy()
    df_fr['Payement_Value'] = df_fr['PAY_SEPT'] + df_fr['PAY_AUG'] + df_fr['PAY_JUL'] + df_fr['PAY_JUN'] + df_fr['PAY_MAY'] + df_fr['PAY_APR']
    df_fr['Dues'] = (df_fr['BILL_AMT_APR']+df_fr['BILL_AMT_MAY']+df_fr['BILL_AMT_JUN']+df_fr['BILL_AMT_JUL']+df_fr['BILL_AMT_SEPT'])-(df_fr['PAY_AMT_APR']+df_fr['PAY_AMT_MAY']+df_fr['PAY_AMT_JUN']+df_fr['PAY_AMT_JUL']+df_fr['PAY_AMT_AUG']+df_fr['PAY_AMT_SEPT'])
     
    df_fr['EDUCATION']=np.where(df_fr['EDUCATION'] == 6, 4, df_fr['EDUCATION'])
    df_fr['EDUCATION']=np.where(df_fr['EDUCATION'] == 0, 4, df_fr['EDUCATION'])

    df_fr['MARRIAGE']=np.where(df_fr['MARRIAGE'] == 0, 3, df_fr['MARRIAGE'])

    df_fr.replace({'SEX': {1 : 'MALE', 2 : 'FEMALE'}, 'EDUCATION' : {1 : 'graduate school', 2 : 'university', 3 : 'high school', 4 : 'others'}, 'MARRIAGE' : {1 : 'married', 2 : 'single', 3 : 'others'}}, inplace = True)

    df_fr = pd.get_dummies(df_fr,columns=['EDUCATION','MARRIAGE'])
    df_fr.drop(['EDUCATION_others','MARRIAGE_others'],axis = 1, inplace = True)
    df_fr = pd.get_dummies(df_fr, columns = ['PAY_SEPT',	'PAY_AUG',	'PAY_JUL',	'PAY_JUN',	'PAY_MAY',	'PAY_APR'], drop_first = True )

    encoders_nums = {
                 "SEX":{"FEMALE": 0, "MALE": 1}
    }
    df_fr = df_fr.replace(encoders_nums)
    df_fr.drop('ID',axis = 1, inplace = True)
    # df_fr.drop(['Unnamed: 0'],axis = 1, inplace = True)
    return df_fr


def predict(df):
    model_save_name = 'xgb_optimized_classifier.pt'
    path = F"./api/logic/{model_save_name}"
    optimal_xgb = torch.load(os.path.abspath(path))

    # df = clean_data(df)
    df = pd.read_csv(os.path.abspath("./api/logic/Final_df.csv"))
    df = df.drop(['IsDefaulter','Payement_Value','Dues'],axis=1)
    df = df.iloc[:10 , 1:]

    prediction = optimal_xgb.predict_proba(df)[::,1]
    # threshold = 0.5
    # classified_predictions = (prediction >= threshold).astype(int)
    prediction = prediction * 100
    prediction = np.around(prediction, decimals=5)
    return prediction