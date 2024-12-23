'''Escreva um programa que repita a leitura de uma senha até que ela seja válida. 
Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". 
Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002. 

Entrada
A entrada é composta por vários casos de testes contendo valores inteiros.

Saída
Para cada valor lido mostre a mensagem correspondente à descrição do problema.
____________________________________________________________________________________________________________________'''

senha_correta = str(2002)

while(True):
  senha = (input())

  if senha != senha_correta:
      print('Senha Invalida')
  elif senha == senha_correta: break

print('Acesso Permitido')