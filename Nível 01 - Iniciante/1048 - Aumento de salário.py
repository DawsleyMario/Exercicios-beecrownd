'''A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário 
0 - 400.00: 15% reajuste
400.01 - 800.00: 12% reajuste
800.01 - 1200.00 10% reajuste
1200.01 - 2000.00 7% reajuste
Acima de 2000.00: 4% reajuste

Leia o salário do funcionário e calcule e mostre o novo salário, 
bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste 
(ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

https://judge.beecrowd.com/pt/problems/view/1048 
____________________________________________________________________________________________________________________'''


salario = float(input())

if salario > 0 and salario <= 400:
    reajuste = (salario/100) * 15
    print(f'Novo salario: {salario + reajuste:.2f}\n\
Reajuste ganho: {reajuste:.2f}\n\
Em percentual: 15 %')
    
elif salario > 400 and salario <= 800:
    reajuste = (salario/100) * 12
    print(f'Novo salario: {salario + reajuste:.2f}\n\
Reajuste ganho: {reajuste:.2f}\n\
Em percentual: 12 %')
    
elif salario > 800 and salario <= 1200:
    reajuste = (salario/100) * 10
    print(f'Novo salario: {salario + reajuste:.2f}\n\
Reajuste ganho: {reajuste:.2f}\n\
Em percentual: 10 %')
    
elif salario > 1200 and salario <= 2000:
    reajuste = (salario/100) * 7
    print(f'Novo salario: {salario + reajuste:.2f}\n\
Reajuste ganho: {reajuste:.2f}\n\
Em percentual: 7 %')
    
elif salario > 2000:
    reajuste = (salario/100) * 4
    print(f'Novo salario: {salario + reajuste:.2f}\n\
Reajuste ganho: {reajuste:.2f}\n\
Em percentual: 4 %')