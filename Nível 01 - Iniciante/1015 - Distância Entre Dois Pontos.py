'''Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) 
e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

Distancia =

Entrada
O arquivo de entrada contém duas linhas de dados. 
A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.

https://judge.beecrowd.com/pt/problems/view/1015
____________________________________________________________________________________________________________________'''

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

print(f'{(((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5:.4f}')