import matplotlib.pyplot as plt
import numpy as np
from .config import K_RANGE

def plot_error_vs_k(runs_data):
    plt.figure(figsize=(10, 6))
    for i, errors in enumerate(runs_data):
        plt.plot(list(K_RANGE), errors, label=f'Run {i + 1}')
    plt.xlabel('Value of k')
    plt.ylabel('Average Error')
    plt.title('Average Error vs k (3 Runs)')
    plt.xticks(list(K_RANGE))
    plt.legend()
    plt.grid(True)
    plt.show()

# -------------------------------------------------------------------
# AI-assisted code:
# The comparative visualization of both users' error curves was
# implemented with support from generative AI.
# -------------------------------------------------------------------
def plot_error_vs_k_comparison(runs_data_user1, runs_data_user2):
    """Plot comparison of error vs k for two users side by side"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Plot User 1
    for i, errors in enumerate(runs_data_user1):
        axes[0].plot(list(K_RANGE), errors, label=f'Run {i + 1}')
    axes[0].set_xlabel('Value of k')
    axes[0].set_ylabel('Average Error')
    axes[0].set_title('Average Error vs k - User 1 (3 Runs)')
    axes[0].set_xticks(list(K_RANGE))
    axes[0].legend()
    axes[0].grid(True)
    
    # Plot User 2
    for i, errors in enumerate(runs_data_user2):
        axes[1].plot(list(K_RANGE), errors, label=f'Run {i + 1}')
    axes[1].set_xlabel('Value of k')
    axes[1].set_ylabel('Average Error')
    axes[1].set_title('Average Error vs k - User 2 (3 Runs)')
    axes[1].set_xticks(list(K_RANGE))
    axes[1].legend()
    axes[1].grid(True)
    
    plt.tight_layout()
    plt.show()

def print_results(results_df, accuracies):
    print("\nOutput of the recommendation system:")
    print(results_df.to_string(index=False))
    print("\n--- Accuracy summary ---")
    print(f"Accuracies in the 5 iterations: {accuracies}")
    print(f"Average Accuracy: {np.mean(accuracies):.2f}")

def print_results_comparison(results_df_user1, accuracies_user1, results_df_user2, accuracies_user2):
    """Print results for both users for comparison"""
    print("\n" + "="*80)
    print("USER 1 RESULTS")
    print("="*80)
    print("\nRecommendation System Output (User 1):")
    print(results_df_user1.to_string(index=False))
    print("\n--- Accuracy Summary (User 1) ---")
    print(f"Accuracies in the 5 iterations: {accuracies_user1}")
    print(f"Average Accuracy: {np.mean(accuracies_user1):.2f}")
    
    print("\n" + "="*80)
    print("USER 2 RESULTS")
    print("="*80)
    print("\nRecommendation System Output (User 2):")
    print(results_df_user2.to_string(index=False))
    print("\n--- Accuracy Summary (User 2) ---")
    print(f"Accuracies in the 5 iterations: {accuracies_user2}")
    print(f"Average Accuracy: {np.mean(accuracies_user2):.2f}")
    
    print("\n" + "="*80)
    print("COMPARISON")
    print("="*80)
    print(f"Average Accuracy User 1: {np.mean(accuracies_user1):.2f}")
    print(f"Average Accuracy User 2: {np.mean(accuracies_user2):.2f}")
    print(f"Difference: {abs(np.mean(accuracies_user1) - np.mean(accuracies_user2)):.2f}")