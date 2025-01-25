from fastapi import FastAPI
from pydantic import BaseModel
import model


class Transaction(BaseModel):
    trans_date_trans_time: str
    cc_num: int
    merchant: str
    category: str
    trans_amount: float
    first_name: str
    last_name: str
    gender: str
    street: str
    city: str
    state_code: str
    zip: int
    city_population: int
    job: str
    dob: str


app = FastAPI()


@app.post("/transaction/")
async def create_item(transaction: Transaction):
    trans_dict = transaction.dict()
    df = model.read_data(trans_dict)
    # preprocessing data
    df = model.preprocessing_data(df)
    # numerical data
    df = model.str_to_int(df, '../ordinal_encoder.pkl')
    # scaling data
    X_test = model.scaling_data(df, '../scaler.pkl')
    # X_test = X_test.values
    print(X_test)
    # predicting
    prediction = model.eval_model(X_test, '../xgboost_model.pkl')
    return {"prediction": int(prediction[0])}
