import pandas as pd
from sklearn.model_selection import train_test_split
from .config import DATA_PATH, CSV_SEPARATOR, DROP_COLUMNS, UNSEEN_SPLIT

def load_data():
    df = pd.read_csv(DATA_PATH, sep=CSV_SEPARATOR, skipinitialspace=True)
    X = df.drop(columns=DROP_COLUMNS)
    y1 = df['rating_user1']
    y2 = df['rating_user2']
    movies = df['Movie']
    return X, y1, y2, movies

def split_unseen(X, y1, y2, movies, random_state=None):
    return train_test_split(
        X, y1, y2, movies,
        test_size=UNSEEN_SPLIT,
        random_state=random_state
    )