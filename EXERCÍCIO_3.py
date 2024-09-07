#3) Os pares de instruções abaixo produzem o mesmo resultado?
# Imprima os valores abaixo, veja se algum deles (A, B ou C) possuem valores diferentes
# nas versões 1 e 2, e caso sim, explique num comentário o motivo.

a1 = (4/2)+(2/4)
b1 = 4/(2+2)/4
c1 = (4+2)*2-4
a2 = 4/2+2/4
b2 = 4/2+2/4
c2 = 4+2*2-4
print(f'{a1} e {a2}; {b1} e {b2}; {c1} e {c2}')

# NA B1 E B2 NÃO FOI O MESMO RESULTADO POIS NA B1 NO CALCULO DE 2+2
# POSSUI PARÊNTESES . NA ÁREA DE OPERADORES ARITMÉTICOS, EXISTE UMA
# ORDEM DE PRESCEDÊNCIA, E NELA DIZ QUE TODA A OPERAÇÃO QUE ESTÁ ENTRE
# PARÊNTESES É EXECUTADA PRIMEIRO . POR ISSO A DIFERENÇA:

# C1 E C2 É BASICAMENTE O MESMO RACIOCÍNIO . NA C1 UM CALCULO ENTRE PARÊNTESES (4+2)
# E ELE SERÁ EXECUTADO PRIMEIRO
