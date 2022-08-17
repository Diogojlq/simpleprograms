import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c' :
        if low != high:   
            guess = random.randint(low,high)
        else:
            guess = low
        guess = random.randint(low,high) #randint = o computador escolhe um numero inteiro aleatorio entre low(1) e high(x)
        feedback = input(f'Is {guess} too high(H),too low(L),or correct (C) ?? ').lower()
        if feedback == 'h' :
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Eba ! O computador acertou o numero,{guess},corretamente!')

computer_guess(10)