# número secreto
import random
numSecreto=random.randint(1, 10)
x=int(input("Adivinhe um número secreto entre 1 e 10: "))
if x==numSecreto:
    print("Parabéns! Você acertou o número secreto.")
elif x<numSecreto:
    print(f"O número secreto é maior que: {x}")
else:
    print(f"O número secreto é menor que: {x}")