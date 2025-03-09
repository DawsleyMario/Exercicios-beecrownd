'''Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. 
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. 
Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.

https://judge.beecrowd.com/pt/problems/view/1020
____________________________________________________________________________________________________________________'''

anos = 0
meses = 0
dias = 0

entrada = int(input())

while True:
    if entrada >= 365:
        anos += 1
        entrada -= 365
    if entrada >= 30:
        meses += 1
        entrada -= 30
    if entrada >= 1:
        dias += 1
        entrada -= 1
    else:
        break

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')