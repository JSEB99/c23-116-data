import pandas as pd
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
import xgboost as xgb
import joblib


def read_data(datos) -> pd.DataFrame:
    df = pd.DataFrame([datos])
    return df


def get_card_type(card_number):
    card_number = str(card_number)  # Convertir a cadena
    if card_number.startswith('4'):
        return 'Visa'
    elif card_number[:2] in ('51', '52', '53', '54', '55') or 2221 <= int(card_number[:4]) <= 2720:
        return 'Mastercard'
    elif card_number[:2] in ('34', '37'):
        return 'American Express'
    elif card_number.startswith('6011') or card_number[:3] in [str(x) for x in range(644, 650)] or card_number.startswith('65') or 622126 <= int(card_number[:6]) <= 622925:
        return 'Discover'
    elif 3528 <= int(card_number[:4]) <= 3589:
        return 'JCB'
    elif card_number[:2] in ('36', '38') or card_number[:3] in ('300', '301', '302', '303', '304', '305'):
        return 'Diners Club'
    else:
        return 'Unknown'


def date_cols(dataframe: pd.DataFrame) -> pd.DataFrame:
    # date of birth
    dataframe["dob"] = pd.to_datetime(dataframe["dob"])
    dataframe.dropna(subset=["dob"], inplace=True)
    dataframe["birth_year"] = dataframe.loc[:, "dob"].dt.year
    dataframe["birth_month"] = dataframe.loc[:, "dob"].dt.month
    print("Date of birth date columns created")
    # transaction date & time
    dataframe["trans_date_trans_time"] = pd.to_datetime(
        dataframe["trans_date_trans_time"], errors="coerce")
    dataframe["trans_date_trans_time"].dropna(inplace=True)
    dataframe["trans_year"] = dataframe.loc[:,
                                            "trans_date_trans_time"].dt.year
    dataframe["trans_month"] = dataframe.loc[:,
                                             "trans_date_trans_time"].dt.month
    dataframe["trans_day"] = dataframe.loc[:,
                                           "trans_date_trans_time"].dt.day
    dataframe["trans_dayofweek"] = dataframe.loc[:,
                                                 "trans_date_trans_time"].dt.dayofweek
    dataframe["trans_hour"] = dataframe.loc[:,
                                            "trans_date_trans_time"].dt.hour
    print("Transaction date columns created.")
    return dataframe


def group_column(column: pd.Series, column_name: str, uniqueness: bool) -> pd.Series:
    trans_percentiles = [4.11, 7.73, 15.66, 32.0, 47.4, 60.84, 74.95,
                         94.492, 136.44, 195.95, 544.6102, 5221.3922, 14334.0299]
    city_percentiles = [260.0, 568.0, 964.0, 1631.0,
                        2456.0, 4726.0, 10076.0, 42619.0, 186140.0, 525713.0]
    # Asignamos la lista de percentiles según el nombre de la columna
    if column_name == "trans_amount":
        percentiles = trans_percentiles
    elif column_name == "city_population":
        percentiles = city_percentiles
    else:
        raise ValueError(
            "column_name must be either 'trans_amount' or 'city_population'")

    # Si es un solo valor, buscamos el percentil correspondiente
    if uniqueness:
        value = column.iloc[0]  # Obtienes el valor si solo hay uno

        # Buscar el valor de percentil correspondiente
        for percentile in percentiles:
            if value <= percentile:
                # Devuelves el valor del percentil
                return pd.Series([percentile])

        # Si no se encontró el percentil, lo asignamos al último
        return pd.Series([percentiles[-1]])


def preprocessing_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    # filtro
    print("filtering columns...")
    selected_cols = ['trans_date_trans_time', 'cc_num', 'category', 'trans_amount', 'gender',
                     'city', 'state_code', 'city_population', 'job', 'dob']
    df = dataframe[selected_cols]
    print("Columns filtered!\nCreating date columns...")
    df = date_cols(df.copy())
    print("Date columns created.\nCategorizing credit cards...")
    # Aplicar la función a la columna
    df['cc_num'] = df['cc_num'].apply(get_card_type)
    print("Credit cards categorized.\nReducing transactions...")
    df["trans_amount_cat"] = group_column(
        df["trans_amount"], "trans_amount", True)
    print("Transactions reduced\nCity Population reducing...")
    df["city_pop_cat"] = group_column(
        df["city_population"], "city_population", True)
    print("City population reduced\nFinal touches...")
    final_cols = ['cc_num', 'category', 'gender', 'city', 'state_code',
                  'job', 'birth_year', 'birth_month', 'trans_year',
                  'trans_month', 'trans_day', 'trans_dayofweek', 'trans_hour', 'trans_amount_cat',
                  'city_pop_cat']
    df = df[final_cols]
    print("Executed!")
    return df


def str_to_int(dataframe: pd.DataFrame, encoder_path: str) -> pd.DataFrame:
    categorical_cols = dataframe.select_dtypes(include=['object']).columns

    encoder = joblib.load(encoder_path)

    dataframe[categorical_cols] = encoder.transform(
        dataframe[categorical_cols])

    return dataframe


def scaling_data(dataframe: pd.DataFrame, scaler_path: str):
    # Separar el target y las características
    X_test = dataframe

    # Escalar las columnas numéricas
    scaler = joblib.load(scaler_path)

    X_test_scaled = scaler.transform(X_test)

    return X_test_scaled


def eval_model(X_test, model_path: str):

    model = joblib.load(model_path)
    # Predicciones
    y_pred = model.predict(X_test)

    return y_pred
