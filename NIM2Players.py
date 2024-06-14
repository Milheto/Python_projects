import random as r

def exibeApresentacaoJogo():
    print('***' + 52*' ' + '***')
    print('***'+22*' ' +'Jogo NIM' + 22*' ' + '***')
    print('***'+9*' ' +'Vence quem retirar o último bastão' + 9*' ' + '***')
    print('***'+22*' ' +'Boa Sorte!!!' + 18*' ' + '***')
    print('***' + 52*' ' + '***')
    
def geraListaBastoes():
    qtdGrupos = r.randint(3,6)
    l = []
    for i in range(qtdGrupos):
        a = r.randint(1,7)
        l.append(a)
        
    return l

def exibeBastoes(l):
    for i,el in enumerate(l):
        print(f'Grupo {i + 1}: ',end='')
        for el in range(el):
            print(chr(9608),end = ' ')
        
        print('\n')
        
def umaJogada(l,p):
    g = int(input(f'Jogador {p + 1}, de qual grupo que voce deseja remover?'))
    q = int(input('Quantos bastões desse grupo voce deseja remover?'))
    g -= 1
    l[g] = l[g] - q
    return sum(l) == 0

def game(l,p):
    exibeBastoes(l)
         
    a = umaJogada(l, p)   
        
    if a != True:
        
        p = (p+1) % 2
        
        game(l,p)
    else:
        
        print(f'Jogador {p+1} Ganhou!')
    


    
exibeApresentacaoJogo()
p = 0
l = geraListaBastoes()
game(l,p)