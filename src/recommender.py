import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from .config import K_RANGE, N_RUNS, TEST_SPLIT

def find_optimal_k(X_reduced, y_reduced):

    best_k = 1
    min_error = float('inf')
    runs_data = []  # [(errors_list), ...]

    for _ in range(N_RUNS):
        X_train, X_test, y_train, y_test = train_test_split(
            X_reduced, y_reduced, test_size=TEST_SPLIT
        )
        errors = []
        for k in K_RANGE:
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(X_train, y_train)
            y_pred = knn.predict(X_test)
            errors.append(np.mean(y_pred != y_test))

        runs_data.append(errors)
        local_min = min(errors)
        if local_min < min_error:
            min_error = local_min
            best_k = list(K_RANGE)[errors.index(local_min)]

    return best_k, runs_data

def run_final_test(X_reduced, y_reduced, X_unseen, y_unseen, movies_unseen, best_k, n_runs):

    accuracies = []
    results_df = None

    for i in range(n_runs):
        knn = KNeighborsClassifier(n_neighbors=best_k)
        knn.fit(X_reduced, y_reduced)
        y_pred = knn.predict(X_unseen)
        accuracies.append(accuracy_score(y_unseen, y_pred))

        if i == 0:
            results_df = pd.DataFrame({
                'Movie title (10% data set)': movies_unseen.values,
                'Recommendation by the classifier': y_pred,
                'Known values': y_unseen.values
            })

    return accuracies, results_df