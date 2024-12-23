'''Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. 
O último dado, que não entrará nos cálculos, contém o valor de idade negativa. 
Calcular e imprimir a idade média deste grupo de indivíduos.

Entrada
A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.

Saída
A saída contém um valor correspondente à média de idade dos indivíduos.

A média deve ser impressa com dois dígitos após o ponto decimal.
____________________________________________________________________________________________________________________'''

idade = []

while(True):
  numero = int(input())
    
  if numero > 0:
      idade.append(numero)
  else: break

quant_medias = len(idade)
soma_idade = sum(idade)

print(f'{(soma_idade / quant_medias):.2f}')
