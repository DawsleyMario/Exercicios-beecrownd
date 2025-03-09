'''Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  
Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

https://judge.beecrowd.com/pt/problems/view/1049
____________________________________________________________________________________________________________________'''

aguia = ('vertebrado', 'ave', 'carnivoro')
pomba = ('vertebrado', 'ave', 'onivoro')
homem = ('vertebrado', 'mamifero', 'onivoro')
vaca = ('vertebrado', 'mamifero', 'herbivoro')
pulga = ('invertebrado', 'inseto', 'hematofago')
lagarta = ('invertebrado', 'inseto', 'herbivoro')
sanguessuga = ('invertebrado', 'anelideo', 'hematofago')
minhoca = ('invertebrado', 'anelideo', 'onivoro')

contador = 3
definidores = []
while contador != 0:
    definidores.append(input())
    contador = contador - 1

definidores_ = tuple(definidores)

lista_de_animais = {(aguia) : 'aguia',
                    (pomba) : 'pomba',
                    (homem) : 'homem',
                    (vaca) : 'vaca',
                    (pulga) : 'pulga',
                    (lagarta) : 'lagarta',
                    (sanguessuga) : 'sanguessuga',
                    (minhoca) : 'minhoca'}
print(lista_de_animais[(definidores_)])