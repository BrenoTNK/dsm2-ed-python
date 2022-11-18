from lib.deque import Deque

deque = Deque()

deque.insert_back('Aldovander')
deque.insert_back('Olentina')
deque.insert_back('Galdêncio')
deque.insert_back('Hildebrando')
deque.insert_back('Iranildes')

print(deque)

removido_frente = deque.remove_front()
print('Removido frente:', removido_frente)
print(deque)

deque.insert_back('Turíbio')
print(deque)

primeiro = deque.peek_front()
print('Primeiro da fila:', primeiro)
print(deque)

# Até este ponto, o Deque está sendo usado como uma fila comum

# Inserção prioritária
deque.insert_front('Emerenciana')
print(deque)

# Desistência da fila
desistente = deque.remove_back()
print('Desistente:', desistente)
print(deque)

# Nova inserção prioritária
deque.insert_front('Deusdete')
print(deque)

# Consultado a última pessoa da fila
ultimo = deque.peek_back()
print('Último:', ultimo)
print(deque)

'''
    Pilha |
    Fila  | Baseadas em lista
    Deque |
'''
