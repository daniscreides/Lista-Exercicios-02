"""
Numa fábrica, os trabalhadores são divididos em 3 classes:
os que fazem até 30 peças por mês (Classe C)
os que fazem de 31 a 44 peças por mês (Classe B)
os que fazem mais de 44 peças por mês (Classe A)
A classe C recebe apenas o salário-mínimo (SM).  A classe B recebe SM + 5% do SM.  A classe A recebe SM + 15% do SM.
Faça um programa que:
   Leia Salário Mínimo, Nome do funcionário e o nº de peças fabricadas por mês;
   Calcule o salário final do funcionário e, ainda, imprima a classe que o funcionário pertence;
 A saída do sistema deve ter o seguinte formato:
Funcionário: <FULANO>
Salário Mínimo  (R$):  <SM>
Número de peças fabricadas: <X>           
Classe: <A, B ou C>
Salário final calculado (R$): <Y>

"""
funcionario = input("Nome do Funcionário: ")
salario = float(input("Salário: "))
pecas = int (input("Nº Peças Produzidas: "))

classe = "X"
comissao = 0

if pecas <= 30:
  classe = "C"
  comissao = 0
elif pecas > 30 and pecas <= 44:
  classe = "B"
  comissao = 0.05
else:
  classe = "A"
  comissao = 0.15

salario_comissao = (salario * comissao) + salario

print ("FUNCIONÁRIO: " + funcionario)
print ("SALÁRIO MÍNIMO: " + str(salario))
print ("PEÇAS PRODUZIDAS: " + str(pecas))
print ("CLASSE: " + classe)
print ("SALÁRIO COM COMISSÃO: " + str(salario_comissao))
