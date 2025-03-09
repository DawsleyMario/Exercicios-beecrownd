'''Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. 
Escreva um algoritmo para ler o tipo de combustível abastecido 
(codificado da seguinte forma: 
 1.Álcool 
 2.Gasolina 
 3.Diesel 
 4.Fim). 
Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). 
O programa será encerrado quando o código informado for o número 4.

Entrada
A entrada contém apenas valores inteiros e positivos.

Saída
Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme exemplo.

https://judge.beecrowd.com/pt/problems/view/1134
____________________________________________________________________________________________________________________'''

alcool = []
gasolina = []
diesel = []

while(True):
  numero = int(input())

  if numero == 1:
      alcool.append(numero)
  elif numero == 2:
      gasolina.append(numero)
  elif numero == 3:
      diesel.append(numero)
  elif numero == 4: break


print(f'MUITO OBRIGADO\nAlcool: {len(alcool)}\nGasolina: {len(gasolina)}\nDiesel: {len(diesel)}')