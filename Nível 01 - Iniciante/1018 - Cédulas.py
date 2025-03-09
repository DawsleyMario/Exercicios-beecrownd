'''Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. 
Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

https://judge.beecrowd.com/pt/problems/view/1018 
____________________________________________________________________________________________________________________'''

valor = int(input())
print(valor)

nota_100 = valor // 100
valor = valor % 100
nota_50 = valor // 50
valor = valor % 50
nota_20 = valor // 20
valor = valor % 20
nota_10 = valor // 10
valor = valor % 10
nota_5 = valor // 5
valor = valor % 5
nota_2 = valor // 2
valor = valor % 2
nota_1 = valor // 1
valor = valor % 1

print(f'{nota_100} nota(s) de R$ 100,00\n\
{nota_50} nota(s) de R$ 50,00\n\
{nota_20} nota(s) de R$ 20,00\n\
{nota_10} nota(s) de R$ 10,00\n\
{nota_5} nota(s) de R$ 5,00\n\
{nota_2} nota(s) de R$ 2,00\n\
{nota_1} nota(s) de R$ 1,00')