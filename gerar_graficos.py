"""Gerar gráficos"""

import matplotlib.pyplot as plt


def gerar_grafico(x, tempos_bubble, tempos_merge, tempos_quick):
    """Função gerando os gráficos de cada uma das estruturas de dados"""
    plt.plot(x, tempos_bubble, label='Bubble Sort')
    plt.plot(x, tempos_merge, label='Merge Sort')
    plt.plot(x, tempos_quick, label='Quick Sort')
    plt.xlabel('Número de dados')
    plt.ylabel('Tempo de execução (s)')
    plt.yscale('log')
    plt.legend()
    plt.show()
