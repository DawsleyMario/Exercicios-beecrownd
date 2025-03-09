'''Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. 
Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.

https://judge.beecrowd.com/pt/problems/view/1047 
____________________________________________________________________________________________________________________'''

valores = input()
valores_sep = valores.split()
a, b, c = map(float, valores_sep)

if a + b > c and b + c > a and a + c > b:
    print(f'Perimetro = {a + b + c:.1f}')
else:
    print(f'Area = {(a + b) * c /2:.1f}')