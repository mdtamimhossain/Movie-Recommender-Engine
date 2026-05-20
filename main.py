from src.data_loader import load_data, split_unseen
from src.recommender import find_optimal_k, run_final_test
from src.utils import plot_error_vs_k, print_results
from src.config import N_FINAL_RUNS

def main():

    X, y, movies = load_data()

    X_reduced, X_unseen, y_reduced, y_unseen, movies_reduced, movies_unseen = \
        split_unseen(X, y, movies)

    best_k, runs_data = find_optimal_k(X_reduced, y_reduced)
    print(f"-> k ótimo selecionado: {best_k}")
    plot_error_vs_k(runs_data)

    accuracies, results_df = run_final_test(
        X_reduced, y_reduced, X_unseen, y_unseen, movies_unseen, best_k, N_FINAL_RUNS
    )
    print_results(results_df, accuracies)

if __name__ == '__main__':
    main()