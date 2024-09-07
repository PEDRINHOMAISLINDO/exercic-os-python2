
inicio
    ler nome
    ler sexo
        se sexo = M então
        peso_ideal = (72.7 * altura) - 58
senão peso_ideal = (62.1 * altura) – 44.7
fim_se
escrever peso_ideal
fim


# forma correta
ALGORITMO: "PESO IDEAL"
VARIAVEIS:
nome, sexo:caractere
peso_real, altura: real
INICIO:
escreva("qual seu nome: ")
leia(nome)
escreva("qual seu sexo: ")
leia(sexo)
escreva("qual sua altura: ")
leia(altura)
se sexo = "feminino" entao
   peso_real <- (62.1 * altura) – 44.7
   escreva("o peso ideial seria ",peso_real)
senao
   peso_real <- (72.7 * altura) - 58
   escreva(" o peso ideal seria ",peso_real)
fimse
FIMALGORITMO: