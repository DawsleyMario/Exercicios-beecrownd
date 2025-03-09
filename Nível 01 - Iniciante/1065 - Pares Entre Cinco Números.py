'''Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.'

'https://judge.beecrowd.com/pt/problems/view/1065 
____________________________________________________________________________________________________________________'''

valores_positivos = []
contador = 0

while contador <= 4:
    numero = int(input())
    if numero % 2 == 0:
        valores_positivos.append(numero)
    contador += 1
print(f'{len(valores_positivos)} valores pares')