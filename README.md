# Análise de Desempenho de Algoritmos de Ordenação

Este repositório contém o código e os gráficos gerados para a comparação de desempenho entre os algoritmos de ordenação **Bubble Sort**, **Merge Sort** e **Quick Sort**.

## Descrição

O objetivo deste trabalho é analisar o desempenho prático de diferentes algoritmos de ordenação em conjuntos de dados de tamanhos variados. A análise é baseada no tempo de execução medido para cada algoritmo ao ordenar listas de datas geradas aleatoriamente.

### Algoritmos analisados:

- **Bubble Sort**: Algoritmo de ordenação simples com complexidade de tempo \(O(n^2)\).
- **Merge Sort**: Algoritmo de ordenação eficiente com complexidade de tempo \(O(n \log n)\).
- **Quick Sort**: Um dos algoritmos de ordenação mais rápidos na prática, com complexidade de tempo média \(O(n \log n)\).

## Organização do Projeto

- `main.py`: Código principal que gera os dados, mede os tempos de execução e chama a função para gerar os gráficos.
- `gerar_graficos.py`: Função responsável por gerar os gráficos com os resultados da análise.
- `gerar_datas.py`: Função que gera listas de datas aleatórias para teste dos algoritmos.
- `algoritmos_ordenacao.py`: Implementações dos algoritmos de ordenação.
- `medir_tempo.py`: Função para medir o tempo de execução dos algoritmos.
- `Figure_1.png`: Gráfico gerado que compara o tempo de execução dos três algoritmos com diferentes quantidades de dados.

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
