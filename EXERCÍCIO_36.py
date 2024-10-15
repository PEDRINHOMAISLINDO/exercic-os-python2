print('=-' * 25)
print('DOIS HOMENS E DUAS MULHERES')
print('=-' * 25)
homem_1 = int(input('DIGITE A IDADE DO PRIMEIRO HOMEM: '))
print('=-' * 25)
homem_2 = int(input('DIGITE A IDADE DO SEGUNDO HOMEM: '))
print('=-' * 25)

while homem_1 == homem_2:
    print('''NÚMEROS REPETIDOS
    DIGITE OS NÚMEROS NOVAMENTE!''')
    print('=-' * 25)
    homem_1 = int(input('DIGITE A IDADE DO PRIMEIRO HOMEM: '))
    print('=-' * 25)
    homem_2 = int(input('DIGITE A IDADE DO SEGUNDO HOMEM: '))
    print('=-' * 25)

mulher_1 = int(input('DIGITE A IDADE DA PRIMEIRA MULHER: '))
print('=-' * 25)
mulher_2 = int(input('DIGITE A IDADE DA SEGUNDA MULHER: '))

while mulher_1 == mulher_2:
    print('''NÚMEROS REPETIDOS
    DIGITE OS NÚMEROS NOVAMENTE!''')
    print('=-' * 25)
    mulher_1 = int(input('DIGITE A IDADE DA PRIMEIRA MULHER: '))
    print('=-' * 25)
    mulher_2 = int(input('DIGITE A IDADE DA SEGUNDA MULHER: '))

lista_homem = [homem_1, homem_2]
lista_mulher = [mulher_1, mulher_2]
lista_homem.sort()
lista_mulher.sort()

print(f'''A SOMA DO HOMEM MAIS VELHO ({lista_homem[1]}) ANOS COM A MULHER MAIS NOVA ({lista_mulher[0]}) ANOS
É IGUAL A {lista_homem[1] + lista_mulher[0]}''')
print('=-' * 25)
print(f'''A SOMA DO HOMEM MAIS NOVO ({lista_homem[0]}) COM A MULHER MAIS VELHA {lista_mulher[1]}
É IGUAL Á {lista_homem[0] + lista_mulher[1]}''')