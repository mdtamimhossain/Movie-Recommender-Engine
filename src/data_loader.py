import pandas as pd
from sklearn.model_selection import train_test_split
from .config import DATA_PATH, CSV_SEPARATOR, DROP_COLUMNS, UNSEEN_SPLIT, RANDOM_STATE

def load_data():
    df = pd.read_csv(DATA_PATH, sep=CSV_SEPARATOR, skipinitialspace=True)
    X = df.drop(columns=DROP_COLUMNS)
    y = df['rating']
    movies = df['Movie']
    return X, y, movies

def split_unseen(X, y, movies):
    return train_test_split(
        X, y, movies,
        test_size=UNSEEN_SPLIT,
        random_state=RANDOM_STATE
    )