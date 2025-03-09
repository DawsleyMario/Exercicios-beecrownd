'''Leia 3 valores inteiros e ordene-os em ordem crescente. 
No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, 
os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

https://judge.beecrowd.com/pt/problems/view/1042
____________________________________________________________________________________________________________________'''

valores = input()
valores_sep = valores.split()
valores_int = [int(val) for val in valores_sep]
valores_int.sort()
print(f'{valores_int[0]}\n{valores_int[1]}\n{valores_int[2]}\n\n{valores_sep[0]}\n{valores_sep[1]}\n{valores_sep[2]}')