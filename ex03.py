"""Faça um programa para uma escola que, dadas três notas de um aluno e seu nome completo, exiba, no final, o nome do estudante, a média final e o seu conceito, observando que:
a média final é calculada a partir da média aritmética simples das 3 notas;
o conceito é determinado a partir da tabela a seguir:
MÉDIA FINAL
CONCEITO
 80
A
 50 e <80 
B
< 50
C

A mensagem final exibida do sistema deve ter o seguinte formato (substitua os espaços entre <> pelos respectivos valores passado como entrada para o sistema):
“<Fulano de tal> obteve conceito <X>”
“As notas fornecidas como entrada foram: <N1>, <N2> e <N3> com Média final: <M>” """

nome= input("Nome do aluno: ")
nota1= int(input("1ª nota: "))
nota2= int(input("2ª nota: "))
nota3= int(input("3ª nota: "))

media = (nota1 + nota2 + nota3) / 3

conceito = "x"

if media >= 80:
  conceito = "A" 
elif media > 50 and media < 80:
  conceito = "B"
else:
  conceito = "C"

print ( nome + " obteve conceito " + conceito )

print ("As notas fornecidas como entrada foram: " + "(" + str(nota1) + "," + str(nota2) + "," + str(nota3) + ")" + " com média final: " + '"' + str(conceito) + '"')