# número secreto
print("Número Secreto")
print("escolha o nível de dificuldade:")
print("1 - Fácil ")
print("2 - Médio ")
print("3 - Difícil ")

nivel=int(input("Digite o nível desejado (1, 2, 3): "))

import random
numSecreto=random.randint(1, 10)

score=100

if nivel==1:
    tentativas1=30
    print("Você escolheu o nível Fácil.")
    print(numSecreto)
    
    x=int(input("Adivinhe um número secreto entre 1 e 10: "))
    
    while True:
        if x == numSecreto:
            print("PARABÉNS !!! Você acertou o número secreto. A sua pontuação final é de: "+str(score))
            break
        
        else:
            print("Número errado! Tente novamente.")
            tentativas1-=1
            score-=2
            x=int(input(f"Você tem {tentativas1} tentativas restantes. Sua pontuação é de: {score}. Tente adivinhar o número secreto: ")) 
    
        if tentativas1 == 0:
            print("GAME OVER !!! Tentativas excedidas.")
            break


elif nivel==2:
    tentativas2=15
    print("Você escolheu o nível Médio.")    
    x=int(input("Adivinhe um número secreto entre 1 e 10: "))
    while True:
        if x == numSecreto:
            print("PARABÉNS !!! Você acertou o número secreto. A sua pontuação final é de: "+str(score))
            break
        else:
            print("Número errado! Tente novamente.")
            tentativas2-=1
            score-=5
            x=int(input(f"Você tem {tentativas2} tentativas restantes. Sua pontuação é de: {score} Tente adivinhar o número secreto: ")) 
        if tentativas2 == 0:
            print("GAME OVER !!! Tentativas excedidas.")
            break

elif nivel==3:
    tentativas3=5
    print("Você escolheu o nível Difícil.")
    print(numSecreto)    
    x=int(input("Adivinhe um número secreto entre 1 e 10: "))
    while True:
        if x == numSecreto:
            print("PARABÉNS !!! Você acertou o número secreto! A sua pontuação final é de: "+str(score))
            break
        else:
            print("Número errado! Tente novamente.")
            tentativas3-=1
            score-=10
            x=int(input(f"Você tem {tentativas3} tentativas restantes. Sua pontuação é de: {score}. Tente adivinhar o número secreto: ")) 
        if tentativas3 == 0:
            print("GAME OVER !!! Tentativas excedidas.")
            break












