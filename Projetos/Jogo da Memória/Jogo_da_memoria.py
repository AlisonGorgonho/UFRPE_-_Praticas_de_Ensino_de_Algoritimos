#Alison Gorgonho da Silva
#Praticas de ensino de algoritimos
#Atividade 2


#Importando a biblioteca random para tratar dos tabuleiros randomizados
import random

#importando biblioteca time para controlar a visualizacao do tabuleiro
import time

#funcao que cria o tabuleiro preenchido com " X "
def cria_tabuleiro_1(l, c):

    matriz_1 = []

    for i in range(l):
        #cria linha_1
        linha_1 = [] #Lista vazia
        for j in range(c):
            linha_1.append('X')


        #colocando linha na matriz_1
        matriz_1.append(linha_1)

    return matriz_1

#Funcao de imprimir as matrizes
def print_lista(lista):
    for i in lista:
        print i
        print "\n"


#Funcao que cria o tabuleiro(matriz) ja randomizado
def cria_tabuleiro_2(l, c):

    lista_aleatoria = []

    for i in range((l*c)/2):
        lista_aleatoria.append(i+1)
        lista_aleatoria.append(i+1)
        
    random.shuffle(lista_aleatoria)

    matriz_2 = []
    pos = 0
    
    for i in range(l):

        linha_2 = []
        for j in range(c):
                       
            linha_2.append(lista_aleatoria[pos])
            pos+=1
            
        matriz_2.append(linha_2)
              
    return matriz_2


#funcao que realiza as jogadas e define as pontuacoes dos jogadores
def jogadas(lista1, lista2, l, c):

##    global lista_jogadas_validas

    #Lista1 = lista de " X "
    #Lista2 = lista de numeros

    ver_1 = True
    while ver_1:
        
        linha_1 = input("Digite o numero da linha: ")-1
        coluna_1 = input("Digite o numero da coluna: ")-1

        if linha_1 in range(0, l) and coluna_1 in range(0, c):
            ver_1 = False
        else:
            print("Coordenadas fora do range...Digite novamente")

    lista1[linha_1][coluna_1] = lista2[linha_1][coluna_1]

    print_lista(lista1)

    ver_2 = 0


    while ver_2 == 0:
        
        ver_3 = True
        
        while ver_3:
        
            linha_2 = input("Digite o numero da linha: ")-1
            coluna_2 = input("Digite o numero da coluna: ")-1

            if linha_2 in range(0, l) and coluna_2 in range(0, c):
                ver_3 = False
            else:
                print("Coordenadas fora do range...Digite novamente")
 

        if linha_2 == linha_1 and coluna_2 == coluna_1:
            print("Voce digitou as mesmas posicoes ! Digite novamente: \n")
        else:
            ver_2 = 1


    lista1[linha_2][coluna_2] = lista2[linha_2][coluna_2]

    print_lista(lista1)

##    jogada_feita.append(linha_1)
##    jogada_feita.append(coluna_1)
##    jogada_feita.append(linha_2)
##    jogada_feita.append(coluna_2)

##    if jogada_feita in lista_jogadas_validas:
##        print("Voce acabou de passar posicoes que ja foram definidas anteriormente, preste mais atencao !!!")

    if lista2[linha_1][coluna_1] != lista2[linha_2][coluna_2]:
        lista1[linha_1][coluna_1] = " X "
        lista1[linha_2][coluna_2] = " X "

        print("Infelimente voce errou, passe a vez !!!")
        return 0
    
    else:
        print("Parabens, Voce acertou !!!")
##        lista_jogadas_validas.append(jogada_feita)
        return 1


main = True


#loop que chama as funcoes e define as variaveis iniciais
while main:

    l = 4 #Qunatidade de linhas
    c = 5 #Quantidade de colunas

##    ind = 0
##    lista_jogadas_validas = []
##    jogada_feita = []

    tabuleiro_1 = cria_tabuleiro_1(l, c) #Tabuleir de " X "
    tabuleiro_2 = cria_tabuleiro_2(l, c) #Tabuleiro de numeros 
    
    jogador_1 = raw_input("Digite o nome do primeiro jogador: ")#Jogador 1
    jogador_2 = raw_input("Digite o nome do segundo jogador: ")#jogador 2

    score_1 = 0 # pontuacao jogador 1
    score_2 = 0 # pontuacao jogador 2

    while tabuleiro_1 != tabuleiro_2:

        print("%s sua vez de jogar !"%(jogador_1))

        if  jogadas(tabuleiro_1, tabuleiro_2, l, c) == 1:
            score_1+=1

        #Tempo para o jogador visualizar o tabuleiro
        time.sleep(5)
        
        #Comando para 'limpar a tela'
        print ("\n" * 130)
            
        print("%s sua vez de jogar !"%(jogador_2))
        
        if  jogadas(tabuleiro_1, tabuleiro_2, l, c) == 1:
            score_2+=1

##            jogada_feita = [linha_1, coluna_1, linha_2, coluna_2]
##            lista_jogadas_validas.append(jogada_feita)


        #Tempo para o jogador visualizar o tabuleiro
        time.sleep(5)
        
        #Comando para 'limpar a tela'
        print ("\n" * 130)
        
    if score_1 > score_2:
        print("Parabens %s voce ganhou com %d pontos"%(jogador_1, score_1))

    elif score_1 == score_2:
        print("%s empatou com %s"%(jogador_1, jogador_2))

    else:
        print("Parabens %s voce ganhou com %d pontos"%(jogador_2, score_2))

    cond = raw_input("Voce deseja jogar novamente ? (Y/N) ")

    if cond == "N" or cond == "n":
        main = False

        print("Obrigado por jogar.......:)")
