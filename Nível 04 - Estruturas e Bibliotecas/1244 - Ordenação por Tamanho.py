'''Crie um programa para ordenar um conjunto de strings pelo seu tamanho. 
Seu programa deve receber um conjunto de strings e retornar este mesmo conjunto ordenado pelo tamanho das palavras, 
se o tamanho das strings for igual, deve-se manter a ordem original do conjunto.

Entrada
A primeira linha da entrada possui um único inteiro N, que indica o número de casos de teste. 
Cada caso de teste poderá conter de 1 a 50 strings inclusive, e cada uma das strings poderá conter entre 1 e 50 caracteres inclusive. 
Os caracteres poderão ser espaços, letras, ou números.

Saída
A saída deve conter o conjunto de strings da entrada ordenado pelo tamanho das strings. Um espaço em branco deve ser impresso entre duas palavras.

https://judge.beecrowd.com/pt/problems/view/1244
____________________________________________________________________________________________________________________'''

def medidor(frase):
 
  palavras = frase.split()
  palavras_medidas = [(palavra, len(palavra)) for palavra in palavras]
  palavras_medidas.sort(key=lambda x: -x[1])
  palavras_ordenadas = [palavra for palavra, _ in palavras_medidas]
  return print(*palavras_ordenadas)

contador = int(input())
while contador > 0:
    medidor(input())
    contador = contador - 1