'''
    Programa simples que inverte uma palavra e verifica se ela
    é um PALÍNDOMO, isto é, uma palavra que pode ser lida de
    trás para frente assim, como da frente para trás.
    Para isso, usaremos uma estrutura de pilha baseada em uma
    lista do Python.
'''

from lib.stack import Stack

palavra = input('Informe a palavra: ')

# pilha = []  # Lista que será usada como pilha
pilha = Stack()

# 1) Pega cada letra da palavra e coloca na pilha
for letra in palavra:
    # A inserção da letra se dará sempre no final (topo) da pilha
    # pilha.append(letra)
    pilha.push(letra)
    print(pilha)

# Imprimindo a pilha para ver como ficou
print(pilha)

print('-' * 50)

# Variável para receber a palavra remontada e invertida
inverso = ''

# Vamos retirar as letras da pilha, uma a uma, DO FIM PARA O ÍNICIO
# A operação se repete enquanto a pilha não estiver vazia.
# Cada letra retirada é acrescentada à váriavel inverso.
while pilha.is_empty():
    letra = pilha.pop() # Retira o último elemento da pilha
    inverso += letra    # Acrescenta a letra ao inverso
    print(pilha)

print('-' * 50)

print(f'Palavra original: {palavra}')
print(f'Palavra invertida: {inverso}')

if palavra == inverso:
    print('*** A palavra é um palíndromo ***')
else:
    print('--- A palavra NÃO é um palíndromo ---')
