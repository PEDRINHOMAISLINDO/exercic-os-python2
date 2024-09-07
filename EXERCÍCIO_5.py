# Escreva um algoritmo para ler um valor numérico (do teclado)
# e escrever (na tela) o seu antecessor.

#ANTECESSOR:
from time import sleep
from colorama import Fore, init
init()
# init() está iniciando a biblioteca colorama
print(Fore.BLUE + '==' * 25)
#Fore.blue + é uma forma de atribuir cores na str
print(Fore.LIGHTWHITE_EX + 'ANTECESSOR DE UM NÚMERO: ')
print(Fore.BLUE + '==' * 25)
print(Fore.LIGHTWHITE_EX + 'PROCESSANDO...')
sleep(2)
# está "dormindo" por 2 segundos
n1 = int(input('ESCOLHA UM NÚMERO QUALQUER: '))
while n1:
    print(f'O ANTECESSOR DESSE NÚMERO É {n1 - 1}')
    n1 = int(input('ESCOLHA UM NÚMERO QUALQUER: '))






