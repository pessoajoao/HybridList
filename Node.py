class Node:
    ## Construtor
    def __init__(self, dado: object):
        self.carga  = dado
        self.prox   = -1

    ## Retorna uma string
    def __str__(self):
        return str(self.carga)