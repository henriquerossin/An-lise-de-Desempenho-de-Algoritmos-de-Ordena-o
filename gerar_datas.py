"""Gerar Datas"""

import random
from datetime import datetime, timedelta


def gerar_datas_aleatorias(n):
    """Função gerando as datas aleatórias"""
    datas = []
    for _ in range(n):
        data_base = datetime(2020, 1, 1)
        data_aleatoria = data_base + \
            timedelta(days=random.randint(0, 365*3),
                    seconds=random.randint(0, 86400))
        datas.append(data_aleatoria.strftime('%Y-%m-%d %H:%M:%S'))
    return datas
