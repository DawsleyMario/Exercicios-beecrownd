'''Leia quatro valores inteiros A, B, C e D. 
A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.

https://judge.beecrowd.com/pt/problems/view/1007
____________________________________________________________________________________________________________________'''

contador = 4
numeros = []
while contador > 0:
    numeros.append(input())
    contador = contador - 1
print(f"DIFERENCA = {int(numeros[0]) * int(numeros[1]) - int(numeros[2]) * int(numeros[3])}")