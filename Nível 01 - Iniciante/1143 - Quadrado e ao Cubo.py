'''Escreva um programa que leia um valor inteiro N (1 < N < 1000). 
Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.

https://judge.beecrowd.com/pt/problems/view/1143
____________________________________________________________________________________________________________________'''

n = int(input())
for _ in range(1, n+1):
    print(_, _*_, _*_*_)
