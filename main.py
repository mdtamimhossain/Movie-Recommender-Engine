from src.data_loader import load_data, split_unseen
from src.recommender import find_optimal_k, run_final_test
from src.utils import plot_error_vs_k, print_results, plot_error_vs_k_comparison, print_results_comparison
from src.config import N_FINAL_RUNS

def main():

    X, y1, y2, movies = load_data()

    X_reduced, X_unseen, y1_reduced, y1_unseen, y2_reduced, y2_unseen, movies_reduced, movies_unseen = \
        split_unseen(X, y1, y2, movies)

    # Train for both users
    print("\n" + "="*80)
    print("PROCESSING USER 1 (rating_user1)")
    print("="*80)
    best_k_user1, runs_data_user1 = find_optimal_k(X_reduced, y1_reduced)
    print(f"-> best k selected (User 1): {best_k_user1}")

    print("\n" + "="*80)
    print("PROCESSING USER 2 (rating_user2)")
    print("="*80)
    best_k_user2, runs_data_user2 = find_optimal_k(X_reduced, y2_reduced)
    print(f"-> best k selected (User 2): {best_k_user2}")

    # Plot comparison of both users
    print("\nGenerating comparison plot...")
    plot_error_vs_k_comparison(runs_data_user1, runs_data_user2)

    # Final test for both users
    print("\n" + "="*80)
    print("FINAL TEST - USER 1")
    print("="*80)
    accuracies_user1, results_df_user1 = run_final_test(
        X_reduced, y1_reduced, X_unseen, y1_unseen, movies_unseen, best_k_user1, N_FINAL_RUNS
    )

    print("\n" + "="*80)
    print("FINAL TEST - USER 2")
    print("="*80)
    accuracies_user2, results_df_user2 = run_final_test(
        X_reduced, y2_reduced, X_unseen, y2_unseen, movies_unseen, best_k_user2, N_FINAL_RUNS
    )

    # Print comparative results
    print_results_comparison(results_df_user1, accuracies_user1, results_df_user2, accuracies_user2)

if __name__ == '__main__':
    main()