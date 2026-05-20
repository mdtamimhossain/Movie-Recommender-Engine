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

def print_results(results_df, accuracies):
    print("\nOutput of the recommendation system:")
    print(results_df.to_string(index=False))
    print("\n--- Accuracy summary ---")
    print(f"Accuracies in the 5 iterations: {accuracies}")
    print(f"Average Accuracy: {np.mean(accuracies):.2f}")