import random
while True :
    acao_do_usuario = input('pedra, papel ou tesoura ? ')
    possible_actions = ['pedra', 'papel', 'tesoura']
    acao_do_computador = random.choice(possible_actions)


    if acao_do_usuario == acao_do_computador:
        print(f'Os dois jogaram',acao_do_usuario, 'EMPATE')
    elif acao_do_usuario == "pedra" :
        if acao_do_computador == "tesoura":
            print('Pedra ganha de tesoura!Voce venceu')  
        else : 
            print('papel ganha de pedra!Voce perdeu!')
    elif acao_do_usuario == "papel" :
        if acao_do_computador == 'pedra':
            print('papel ganha de pedra!voce venceu!')
        else :
            print('tesoura ganha de papel!voce perdeu!')
    elif acao_do_usuario == "tesoura":
        if acao_do_computador == "papel":
            print('tesoura corta papel!Voce venceu!')
        else:
            print("pedra quebra tesoura!,Voce perdeu.")
    jogar_novamente = input("Jogar novamente ?(S/N): ")
    if jogar_novamente != 'S' :
        break

        
