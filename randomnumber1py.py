import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Advinhe um numero entre 1 e (x): '))
        if guess < random_number:
            print('Desculpe,voce chutou um numero muito baixo.')
        elif guess > random_number:
            print('Desculpe,voce chutou um numero muito alto.')
    
    print(f"Parabeins,voce acertou o numero {random_number}.YEAHH!!")

guess(10) #numero pode ser alterado,pois os numeros validos para a advinhação estao entre 1 e X,e x
            # é o numeor definido ao declarar a funcao ja pronta no final do codigo.
        

    