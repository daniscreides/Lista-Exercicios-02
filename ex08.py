#Escreve um programa em Python que calcule o imposto de renda (IR) final, de acordo com as informações abaixo. Os valores em reais de Salário Bruto e INSS, bem como o Número de dependentes devem ser lidos pelo teclado.
"""Desconto = R$ 90,00 por cada dependente
Base de Cálculo  = Salário Bruto – ( Desconto * Nº de dependentes) – Desconto INSS
IR (em Reais) = (Base de cálculo) * Alíquota – Parcela a deduzir	
Base de Cálculo
Alíquota adicional (%)
Parcela a Deduzir
até 900.80
Isento
R$ 0.00
até 1800.50
15%
R$ 135.00
acima de 1800.50
27.5%
R$ 315.00 """


nome = input ("Nome: ")
salario = float(input("Salário Bruto: "))
inss = float(input("INSS: "))
dependentes = int(input("Número de Dependentes: "))


desconto = (90 * dependentes)
base_cal = (salario - desconto - inss)

aliquota = 0
parcela = 0

if base_cal < 900.80:
  aliquota = 0
  parcela = 0
elif base_cal >= 900.80 and base_cal < 1800.50:
  aliquota = 0.15
  parcela = 135
else:
  aliquota = 0.275
  parcela = 315
  
imposto = (base_cal * aliquota) - parcela

print ("Calculo imposto de renda: " + "R$" + str(imposto))