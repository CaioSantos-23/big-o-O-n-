"""
Exemplo prático de complexidade O(N) — Big O Linear
Integrantes:
  Aline de Brito Simas — 202310031
  Caio dos Santos Silva — 202310328
  Mellani Lyvian de Macêdo dos Santos — 202310725
  Ricardo Ribeiro de Figueiredo — 202310773

Este programa demonstra, na prática, algoritmos com complexidade de
tempo O(N) (linear). Nesse tipo de algoritmo, o número de operações
cresce de forma diretamente proporcional ao tamanho da entrada (N):
se N dobra, o tempo de execução também dobra (aproximadamente).
"""

import time
import random


def soma_linear(lista):
    """
    Soma todos os elementos de uma lista.

    Complexidade: O(N)
    - Um único laço 'for' percorre cada elemento da lista exatamente
      uma vez, executando uma operação de soma por elemento.
    """
    total = 0
    for numero in lista:          # <-- executa N vezes
        total += numero
    return total


def busca_linear(lista, alvo):
    """
    Procura um elemento em uma lista percorrendo item a item.

    Complexidade: O(N)
    - No pior caso (elemento no final da lista ou ausente), o laço
      percorre todos os N elementos antes de concluir.
    """
    for indice, valor in enumerate(lista):
        if valor == alvo:
            return indice
    return -1


def medir_tempo(func, *args):
    inicio = time.perf_counter()
    resultado = func(*args)
    fim = time.perf_counter()
    return resultado, fim - inicio


def demonstracao():
    print("=" * 62)
    print("DEMONSTRAÇÃO PRÁTICA — COMPLEXIDADE O(N)")
    print("=" * 62)

    tamanhos = [1_000, 10_000, 100_000, 1_000_000, 5_000_000]

    print(f"\n{'Tamanho (N)':>15} | {'Tempo soma_linear (s)':>22}")
    print("-" * 42)

    for n in tamanhos:
        lista = [random.randint(1, 100) for _ in range(n)]
        _, tempo = medir_tempo(soma_linear, lista)
        print(f"{n:>15,} | {tempo:>22.6f}")

    print("\nObservação: conforme N aumenta (multiplicado por 10 a cada")
    print("linha), o tempo de execução cresce de forma aproximadamente")
    print("proporcional — essa é a assinatura de um algoritmo O(N).")

    print("\n" + "=" * 62)
    print("Exemplo adicional: busca_linear()")
    print("=" * 62)
    lista_teste = list(range(20))
    alvo = 17
    posicao = busca_linear(lista_teste, alvo)
    print(f"Lista: {lista_teste}")
    print(f"Procurando o valor {alvo} -> encontrado no índice {posicao}")
    print("No pior caso, o algoritmo precisa percorrer todos os N elementos.")


if __name__ == "__main__":
    demonstracao()
