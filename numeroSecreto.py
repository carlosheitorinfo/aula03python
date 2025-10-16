# número secreto
import random
n=random.randint(1, 10)
x=int(input("Adivinhe um número secreto entre 1 e 10: "))
if x==n:
    print("Parabéns! Você acertou o número secreto.")
elif x<n:
    print(f"O número secreto é maior que: {x}")
else:
    print(f"O número secreto é menor que: {x}")