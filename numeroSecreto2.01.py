print("Número Secreto")
print("escolha o nível de dificuldade:")
print("1 - Fácil,\n2 - Médio,\n3 - Difícil")
nivel=int(input("Digite o nível desejado (1, 2, 3): "))
nivel_nomes={1:"Fácil", 2:"Médio", 3:"Difícil"}

import random
numSecreto=random.randint(10, 100)

nivel_tentativas={1:30, 2:15, 3:5}
tentativas=nivel_tentativas.get(nivel, 0)
score=100
nivel_desconto={1:2, 2:5, 3:10}

print(f"Você escolheu o nível {nivel_nomes.get(nivel)}, voce tem {tentativas} tentativas, sua pontuação inicial é de "+str(score))

x=int(input("Adivinhe um número secreto entre 10 e 100: "))
  
while x < 10 or x > 100:
    print("Número inválido! O número deve estar entre 10 e 100.")
    x=int(input("Tente novamente: "))   

while True:
    if x == numSecreto:
        print("PARABÉNS !!! Você acertou o número secreto! A sua pontuação final é de: "+str(score))          
        break
    
    else:
        print("Número errado, tente novamente")
        if x < numSecreto:
            print("o número secreto é maior") 
        else: 
            print("o número secreto é menor")
        tentativas-=1
        score-= (nivel_desconto.get(nivel, 0))
        x=int(input(f"Você tem {tentativas} tentativas restantes. Sua pontuação é de: {score}. Tente adivinhar o número secreto: ")) 
    
    if tentativas == 0:
        print("GAME OVER !!! Tentativas excedidas.")
        break




