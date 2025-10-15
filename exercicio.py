frutas=['maça','banana','laranja']
frutas.append('uva')
print(frutas)
print(frutas[1])
print(len(frutas))
print(frutas[-1])
print(frutas[1:3])
print(frutas.index('laranja'))
frutas.append(22)
print(frutas)
frutas[0]='pera'
print(frutas)
frutas.insert(1,'abacaxi')
print(frutas)
frutas[1:3]=['kiwi','melancia']
print(frutas)
lista=frutas[:] #copia da lista
#lista=frutas #aponta para a mesma lista, o que fizer em uma refelete na outra
print(lista)
print(type(frutas))
print(len(frutas))
frutas.pop(0)
print(frutas)




