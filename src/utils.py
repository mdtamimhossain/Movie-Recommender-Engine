import matplotlib.pyplot as plt
import numpy as np
from .config import K_RANGE

def plot_error_vs_k(runs_data):
    plt.figure(figsize=(10, 6))
    for i, errors in enumerate(runs_data):
        plt.plot(list(K_RANGE), errors, label=f'Run {i + 1}')
    plt.xlabel('Valor de k')
    plt.ylabel('Erro Médio')
    plt.title('Erro Médio vs k (3 Execuções)')
    plt.xticks(list(K_RANGE))
    plt.legend()
    plt.grid(True)
    plt.show()

def print_results(results_df, accuracies):
    print("\nOutput do sistema de recomendação:")
    print(results_df.to_string(index=False))
    print("\n--- Resumo de Acurácia ---")
    print(f"Acurácias nas 5 iterações: {accuracies}")
    print(f"Acurácia Média: {np.mean(accuracies):.2f}")