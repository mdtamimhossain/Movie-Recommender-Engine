import numpy as np

from src.data_loader import load_data, split_unseen
from src.recommender import find_optimal_k, run_final_test
from src.utils import (
    plot_error_vs_k_comparison,
    print_results_comparison
)
from src.config import N_FINAL_RUNS


def main():

    X, y1, y2, movies = load_data()

    accuracies_user1 = []
    accuracies_user2 = []

    final_results_user1 = None
    final_results_user2 = None

    runs_data_user1 = None
    runs_data_user2 = None


# -------------------------------------------------------------------
# AI-assisted code:
# The repeated evaluation workflow using different unseen datasets
# across multiple executions was implemented with AI assistance.
# -------------------------------------------------------------------
    for run in range(N_FINAL_RUNS):

        print("\n" + "=" * 80)
        print(f"FINAL EXECUTION {run + 1}")
        print("=" * 80)

        # NEW RANDOM 10% UNSEEN SET
        (
            X_reduced,
            X_unseen,
            y1_reduced,
            y1_unseen,
            y2_reduced,
            y2_unseen,
            movies_reduced,
            movies_unseen
        ) = split_unseen(
            X,
            y1,
            y2,
            movies,
            random_state=None
        )

        # USER 1
        print("\nPROCESSING USER 1")

        best_k_user1, runs_data_user1 = find_optimal_k(
            X_reduced,
            y1_reduced
        )

        accuracy_user1, results_df_user1 = run_final_test(
            X_reduced,
            y1_reduced,
            X_unseen,
            y1_unseen,
            movies_unseen,
            best_k_user1
        )

        accuracies_user1.append(accuracy_user1)

        # USER 2
        print("\nPROCESSING USER 2")

        best_k_user2, runs_data_user2 = find_optimal_k(
            X_reduced,
            y2_reduced
        )

        accuracy_user2, results_df_user2 = run_final_test(
            X_reduced,
            y2_reduced,
            X_unseen,
            y2_unseen,
            movies_unseen,
            best_k_user2
        )

        accuracies_user2.append(accuracy_user2)

        # save last results for printing
        final_results_user1 = results_df_user1
        final_results_user2 = results_df_user2

    # Plot
    plot_error_vs_k_comparison(
        runs_data_user1,
        runs_data_user2
    )

    # Final report
    print_results_comparison(
        final_results_user1,
        accuracies_user1,
        final_results_user2,
        accuracies_user2
    )

    print("\n")
    print("=" * 80)
    print("FINAL AVERAGES")
    print("=" * 80)

    print(f"Average Accuracy User 1: {np.mean(accuracies_user1):.2f}")

    print(f"Average Accuracy User 2: {np.mean(accuracies_user2):.2f}")


if __name__ == '__main__':
    main()