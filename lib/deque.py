'''
    ESTRUTURA DE DADOS DEQUE

    Deque (Double-Ended Queue) é uma estrutura de dados derivada
    da fila que permite inserções e remoções em qualquer uma de
    suas extremidades. Com isso, o deque pode se comportar tanto
    como uma fila comum quanto como uma fila em que são admitidas
    elementos prioritários e a possibilidade de desistência do
    último elemento.
'''

class Deque:

    ''' Métedo Construtor '''
    def __init__(self):
        self.__data = []    # Lista vazia

    ''' Método de Inserção no Início '''
    def insert_front(self, val):
        self.__data.insert(0, val)

    ''' Método de Inserção no Final '''
    def insert_back(self, val):
        self.__data.append(val)

    ''' Método que Determine se o Deque está Vazio '''
    def is_empty(self):
        return len(self.__data) == 0

    ''' Método de Remoção do Inicio '''
    def remove_front(self):
        if(self.is_empty()):
            raise Exception('ERRO: Impossivel remover de um deque vazio.')
        return self.__data.pop(0)

    ''' Método de Remoção do Final '''
    def remove_back(self):
        if(self.is_empty()):
            raise Exception('ERRO: Impossivel remover de um deque vazio.')
        return self.__data.pop()

    ''' Método que Consulta a Primeira Posição '''
    def peek_front(self):
        if(self.is_empty()):
            raise Exception('ERRO: Impossivel consultar um deque vazio.')
        return self.__data[0]

    ''' Método que Consulta a Última Posição '''
    def peek_back(self):
        if(self.is_empty()):
            raise Exception('ERRO: Impossivel consultar um deque vazio.')
        return self.__data[-1] 

    '''
        Método que permite imprimir a pilha como string
    '''
    def __str__(self):
        return str(self.__data)
