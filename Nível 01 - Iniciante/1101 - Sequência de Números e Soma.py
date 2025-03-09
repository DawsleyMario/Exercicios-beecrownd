'''Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). 
Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

https://judge.beecrowd.com/pt/problems/view/1101 
____________________________________________________________________________________________________________________'''

while True:
    entrada = input()
    numeros = entrada.split()
    a, b = int(numeros[0]), int(numeros[1])

    if a <= 0 or b <= 0:
        break
    if a > b:
        a, b = b, a

    sequencia = list(range(a, b+1))
    soma = sum(sequencia)

    print(*sequencia, f"Sum={soma}")