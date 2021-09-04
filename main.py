from Node import Node
from Lista import Lista, ObjetoInexistenteException

lista1 = Lista()
lista2 = Lista()
lista3 = Lista()
lista4 = Lista()
lista5 = Lista()

padrao = 1
listaPadrao = lista1

while True:
    print("------------------------------------------")
    print("Lista ",padrao,": ",listaPadrao)
    print("------------------------------------------")
    print("(i) Inserir no início")
    print("(f) Inserir no final")
    print("(b) Procurar um valor na lista")
    print("(e) Consultar o conteúdo de um elemento")
    print("(v) Consultar se a lista está vazia")
    print("(s) Obter o tamanho da lista")
    print("(r) Remover do início")
    print("(o) Remover do final")
    print("(p) Imprimir lista")
    print("(m) Mudar a lista")
    print("(x) Sair do programa")
    print()
    opcao = input("Digite uma opção: ")

    if(opcao == 'i'):
        listaPadrao.inserir_inicio(input("Digite aqui: "))
    elif(opcao == 'f'):
        listaPadrao.inserir_final(input("Digite aqui: "))
    elif(opcao == 'b'):
        buscar = input("Buscar Por: ")
        while True:
            try:
                print(buscar, "esta na posição ",listaPadrao.busca(buscar))
            except ObjetoInexistenteException as error:
                print(error)
            else:
                break

    elif(opcao == 'e'):
        while True:
            try:
                while True:
                    try:
                        elm = int(input("Digite a posição: "))
                        print("O elemento encontrado foi o ",listaPadrao.elemento(elm))
                    except IndexError as ierror:
                        print("Não existe essa posição.")
                    else: 
                        break
            except ValueError as error:
                print("Só é permitido numeros naturais.")
            else:
                break

    elif(opcao == 'v'):
        if(listaPadrao.estaVazia()):
            print("Sim")
        else:
            print("Não")
    elif(opcao == 's'):
        print("O tamanho da lista é ", listaPadrao.tamanho())
    elif(opcao == 'r'):
        listaPadrao.remover_inicio()
    elif(opcao == 'o'):
        listaPadrao.remover_final()
    elif(opcao == 'p'):
        print(listaPadrao)
    elif(opcao == 'm'):
        while True:
            try:
                sc = int(input("Qual lista você quer acessar: "))
                padrao = sc
                if(padrao == 1):
                    listaPadrao = lista1
                    break
                elif(padrao == 2):
                    listaPadrao = lista2
                    break
                elif(padrao == 3):
                    listaPadrao = lista3
                    break
                elif(padrao == 4):
                    listaPadrao = lista4
                    break
                elif(padrao == 5):
                    listaPadrao = lista5
                    break
                else:
                    print("Não existe essa lista.")
                    print()
            except ValueError as error:
                print("Digite apenas números.")

    elif(opcao == 'x'):
        break
    else:
        print("Opção não válida.")
        print()