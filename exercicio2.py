aluno = ['Heitor', 50, 1.70]
cabecalho = ['Nome', 'Idade', 'Altura']
print(f"{cabecalho[0]}: {aluno[0]}, {cabecalho[1]}: {aluno[1]}, {cabecalho[2]}: {aluno[2]}")

# Dicionários
pessoa = {'Nome': 'Heitor', 'Idade': 50, 'Altura': 1.70} # {chave: valor}
pessoa['Idade'] = 33
print(pessoa)

diasDaSemana = {1: 'Domingo', 2: 'Segunda', 3: 'Terça', 4: 'Quarta', 5: 'Quinta', 6: 'Sexta'}
print(diasDaSemana)
diasDaSemana[7] = 'Sábado'
print(diasDaSemana)
print(diasDaSemana[4])
print(list(diasDaSemana.keys()))
print(list(diasDaSemana.values()))
for key in diasDaSemana.keys():
    print(key)
for value in diasDaSemana.values():
    print(value)    