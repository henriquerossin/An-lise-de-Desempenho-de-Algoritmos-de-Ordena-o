"""Medir Tempo"""

import time


def medir_tempo(algoritmo, dados):
    """Função medindo o tempo"""
    inicio = time.time()
    algoritmo(dados)
    fim = time.time()
    return fim - inicio
