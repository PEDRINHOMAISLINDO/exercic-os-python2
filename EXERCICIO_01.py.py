# EXERCICIO 01) Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B.
# A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa.
# Ao final, escrever os valores que ficaram armazenados nas variáveis.
A = 10
B = 20
aeb = input(f'a variavel A e igual a {A} e B e igual a {B}, deseja muda-las ? ').strip().capitalize()
if aeb == 'Sim':
    valordea = int(input('ESCOLHA UM VALOR PARA A: '))
    valordeb = int(input('ESCOLHA UM VALOR PARA B: '))
    print(f'Agora os falor de A e {A} e o valor de B e {B}')
elif aeb == 'Nao':
    print(f'Os valores das variaveis continuam, A={A} e B={B}')
exit()


