from colorama import init, Fore # BIBLIOTECA DE CORES

print('**' * 25)
print('SOMA ENTRE OS DOIS MAIORES')
print('**' * 25)
n1 = int(input('DIGITE UM PRIMEIRO NÚMERO: '))
print('**' * 25)
n2 = int(input('DIGITE UM SEGUNDO NÚMERO: '))
print('**' * 25)
n3 = int(input('DIGITE UM TERCEIRO NÚMERO: '))
print('**' * 25)

while n1 == n2 or n2 == n3 or n1 == n3: # ESTRUTURA DE REPETIÇÃO PARA IMPEDIR NÚMEROS IGUAIS.
    print(Fore.LIGHTRED_EX + 'NÃO DIGITE O MESMO NÚMERO!') # FORMA DE ATRIBUIR CORES A UMA STR.
    print(Fore.RESET + '**' * 25)
    n1 = int(input('DIGITE UM PRIMEIRO NÚMERO: '))
    print('**' * 25)
    n2 = int(input('DIGITE UM SEGUNDO NÚMERO: '))
    print('**' * 25)
    n3 = int(input('DIGITE UM TERCEIRO NÚMERO: '))
    print('**' * 25)

lista = [n1, n2, n3] # CRIAÇÃO DE UMA LISTA.
lista.sort() # ORGANIZAR A LISTA DE FORMA CRESCENTE.
print(f'''OS DOIS MAIORES VALORES SÃO {lista[1]} E {lista[2]}.
A SOMA DESSES VALORES VAI DAR {lista[2] + lista[1]}''')

