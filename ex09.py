"""
A diretoria de uma Equipe de Futebol deseja aumentar o salário de seus jogadores registrados.  O ajuste salarial deve obedecer a seguinte tabela:
Salário atual (R$)
Aumento (%)
até 1000.00
30%
até 1500.00
20%
até 2000.00
15%
até 2500.00
10%
acima de 2500.00
5%


Preparar um algoritmo para ler o nome e o salário atual do jogador (em reais) e, no final, possa imprimir seus dados junto com o salário anterior e o novo salário reajustado.
"""

nome= input ("Digite o nome do jogador: ")
salario= float (input("Digite o salário atual do jogador: "))

reajustre= 0


if salario < 1000:
  reajustre= 0.30
if salario >= 1000 and salario < 1500:
  reajustre= 0.20
if salario >= 1500 and salario < 2000:
  reajustre= 0.15
if salario >= 2000 and salario < 2500:
  reajustre= 0.10
else:
  reajustre= 0.05

  aumento= (salario * reajustre) + salario

print ("*REAJUSTRE SALARIAL DO JOGADOR*")
print ("NOME: " + nome)
print ("SALÁRIO ANTERIOR: " + "R$" + str(salario))
print ("SALÁRIO COM REAJUSTRE: " + "R$" + str(aumento))