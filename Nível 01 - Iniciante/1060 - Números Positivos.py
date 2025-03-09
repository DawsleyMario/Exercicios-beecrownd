'''Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). 
A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.

https://judge.beecrowd.com/pt/problems/view/1060 
____________________________________________________________________________________________________________________'''

valores_positivos = []
soma = 0

while soma <= 5:
  numero = float(input())

  if numero >= 0:
      valores_positivos.append(numero)
  soma = soma + 1
print(f'{len(valores_positivos)} valores positivos')