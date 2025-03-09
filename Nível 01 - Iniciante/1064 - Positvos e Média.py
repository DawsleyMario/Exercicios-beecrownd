'''
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. 
Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.

https://judge.beecrowd.com/pt/problems/view/1064 
____________________________________________________________________________________________________________________'''

valores_positivos = []
contador = 0

while contador <= 5:
  numero = float(input())
  if numero >= 0:
      valores_positivos.append(numero)
  contador = contador + 1

print(f'{len(valores_positivos)} valores positivos\n\
{sum(valores_positivos) / len(valores_positivos):.1f}')