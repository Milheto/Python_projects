import random as rd

def exibeApresentacaoJogo():
    print('***' + 52*' ' + '***')
    print('***'+22*' ' +'Jogo NIM' + 22*' ' + '***')
    print('***'+9*' ' +'Vence quem retirar o último bastão' + 9*' ' + '***')
    print('***'+22*' ' +'Boa Sorte!!!' + 18*' ' + '***')
    print('***' + 52*' ' + '***')
    return

def geraListaBastoes():
    l = []  
    for el in range(rd.randint(3,6)):
        l.append(rd.randint(1,7))
    return l

def exibeBastoes(l):
    for el in range(len(l)):
        print(f'\n\nGrupo {el + 1}:', end = '  ')               
        for el2 in range(l[el]):
            print(f'{chr(9608)}', end = ' ')
    return        
                      
def umaJogada(l,jogador):
    j = int(input(f'\n\nJogador {jogador + 1}, de qual grupo deseja retirar os bastoes?'))
    j1 = int(input('Quantos bastoes deseja retirar?'))
    l[j-1] -= j1
    return sum(l) == 0
    
l = geraListaBastoes()

exibeApresentacaoJogo()
exibeBastoes(l)
jogador = 0

while umaJogada(l,jogador) != True:
    jogador = (jogador + 1) % 2
    exibeBastoes(l)
    
print(f'\nO jogador {jogador+1} Ganhou!')
