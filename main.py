"""Main"""

# Importando as funções criadas nos outros arquivos.py
from gerar_datas import gerar_datas_aleatorias
from algoritmos_ordenacao import bubble_sort, merge_sort, quick_sort
from medir_tempo import medir_tempo
from gerar_graficos import gerar_grafico

# Gerando as datas aleatórias
n_dados = [100, 1000, 5000, 10000]
tempos_quick = []
tempos_bubble = []
tempos_merge = []

for n in n_dados:
    datas = gerar_datas_aleatorias(n)

    # Medir tempo dos algoritmos
    tempos_bubble.append(medir_tempo(bubble_sort, datas.copy()))
    tempos_merge.append(medir_tempo(merge_sort, datas.copy()))
    tempos_quick.append(medir_tempo(quick_sort, datas.copy()))

# Gerando o gráfico com as três estruturas de dados executadas
gerar_grafico(n_dados, tempos_bubble, tempos_merge, tempos_quick)
