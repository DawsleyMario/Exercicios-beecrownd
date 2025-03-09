''''Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. 
Utilize a fórmula: MaiorAB = (a+b+abs(a-b)) sob 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

https://judge.beecrowd.com/pt/problems/view/1013 
____________________________________________________________________________________________________________________'''

entrada = input()
valores_sep = entrada.split()
A, B, C = map(int, valores_sep)
maior = max(A, B, C)
print(f'{maior} eh o maior')