# Exemplo prático de complexidade O(N)

## Integrantes

| Nome | Matrícula |
|---|---|
| Aline de Brito Simas | 202310031 |
| Caio dos Santos Silva | 202310328 |
| Mellani Lyvian de Macêdo dos Santos | 202310725 |
| Ricardo Ribeiro de Figueiredo | 202310773 |

## O que é O(N)?

Um algoritmo tem complexidade **O(N)** (linear) quando o número de
operações necessárias cresce de forma **diretamente proporcional**
ao tamanho da entrada (N). Se N dobra, o tempo de execução também
dobra (aproximadamente).

## O que o código faz

O arquivo `big_o_n.py` traz dois exemplos clássicos de O(N):

1. **`soma_linear(lista)`** — percorre a lista uma única vez, somando
   cada elemento. Um laço `for` que executa exatamente N vezes.
2. **`busca_linear(lista, alvo)`** — procura um valor item a item.
   No pior caso, percorre todos os N elementos.

A função `demonstracao()` roda `soma_linear` com listas de tamanhos
crescentes (1 mil, 10 mil, 100 mil, 1 milhão e 5 milhões de itens) e
mede o tempo de execução de cada uma, mostrando na prática que o
tempo cresce proporcionalmente ao tamanho da entrada.

## Como executar

```bash
python3 big_o_n.py
```

## Resultado observado

| N (tamanho) | Tempo (s) |
|---|---|
| 1.000 | ~0,00002 |
| 10.000 | ~0,00018 |
| 100.000 | ~0,0019 |
| 1.000.000 | ~0,019 |
| 5.000.000 | ~0,094 |

O tempo cresce de forma aproximadamente proporcional ao N — a
assinatura de um algoritmo **O(N)**.

