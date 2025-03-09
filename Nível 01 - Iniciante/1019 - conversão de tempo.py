'''Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, 
e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido. 

https://judge.beecrowd.com/pt/problems/view/1019
____________________________________________________________________________________________________________________'''


segundos = int(input())

horas = 0
minutos = 0

while(segundos >= 3600):
    segundos -= 3600
    horas += 1

while(segundos >= 60):
    segundos -= 60
    minutos += 1

print(f'{horas}:{minutos}:{segundos}')