from Node import Node

class ObjetoInexistenteException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Lista:

    ## Construtor
    def __init__(self):
        self.vetor = []
        self.head = None

    ## Verifica se a lista está vazia
    def estaVazia(self):
        if(len(self.vetor) == 0):
            return True
        
        return False

    ## Retorna o tamanho da lista
    def tamanho(self):
        return len(self.vetor)
    
    ## Mostra o elemento na posição que for passada como argumento
    def elemento(self, posicao):
        return self.vetor[posicao]
    
    ## Busca e retorna a posição de um determinado elemento
    def busca(self, valor):
        posicao = 1
        if(valor == self.head.carga):
            return posicao

        atual = self.vetor[self.head.prox]
        while(True):
            posicao += 1

            if(atual.carga == valor):
                return posicao
            else:
                atual = self.vetor[atual.prox]

        raise ObjetoInexistenteException("Não encontrado.")

    ## Insere um elemento no inicio da lista
    def inserir_inicio(self, valor):
        node = Node(valor)
        if(self.head is None):
            self.head = node
            self.vetor.append(self.head)
        
        else:
            posicao = self.vetor.index(self.head)
            node.prox = posicao
            self.head = node
            self.vetor.append(self.head)

    ## Insere um elemento no Final da lista 
    def inserir_final(self, valor):
        node = Node(valor)
        if(self.head is None):
            self.head = node
            self.vetor.append(self.head)
        
        else:
            for i in range(len(self.vetor)):
                if(self.vetor[i].prox == -1):
                    self.vetor[i].prox = len(self.vetor)
            
            self.vetor.append(node)
    
    ## Remove o primeiro elemento da lista
    def remover_inicio(self):
        if(self.head is None):
            print("Lista esta vazia.")
            return

        if(self.head.prox == -1):
            self.vetor.remove(self.head)
            self.head = None
        
        item = self.vetor[self.head.prox]
        self.vetor.remove(self.head)
        self.head = item

    ## Remove O ultimo elemento da lista
    def remover_final(self):
        if(self.head is None):
            print("Lista esta vazia.")
            return

        if(self.head.prox == -1):
            self.vetor.remove(self.head)
            self.head = None
        
        ultimo             = None
        indiceDoUltimo     = 0

        for node in self.vetor:
            if(node.prox == -1):
                ultimo = node
                indiceDoUltimo = self.vetor.index(ultimo)

        self.vetor.remove(ultimo)
        for i in range(len(self.vetor)):
            if(self.vetor[i].prox == indiceDoUltimo):
                self.vetor[i].prox = -1

    ## Retorna uma strig com todos os elementos da lista
    def __str__(self):
        if self.head is None:
            return str("[]")

        if(len(self.vetor) == 1):
            return f'[{self.head}]' 

        texto = f'[{self.head}'
        proximo = self.head

        while True:
            texto += f',{self.vetor[proximo.prox]}'
            proximo = self.vetor[proximo.prox]

            if(proximo.prox == -1):
                texto += f']'
                break


        ##texto += f'{proximo}]'

        return texto