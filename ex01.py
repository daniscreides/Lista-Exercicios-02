#Em um sistema de supermercado, as maçãs custam R$1.50 cada, se forem compradas menos de uma dúzia; e custam R$ 1.10 cada, se o cliente comprar a partir de 12 maçãs. Escreva um algoritmo que leia a quantidade de maçãs compradas pelo cliente, calcule e escreva o custo total da compra.


maca = int(input( "Digite quantidade de maça: " ))

maca_unidade = 1.50
maca_duzia = 1.10

valor_total_unidade = (maca_unidade * maca)
valor_total_duzia = (maca_duzia * maca)

if maca < 12:
  print ("R$"+"{:.2f}".format (valor_total_unidade))
else:
  print ("R$"+"{:.2f}".format (valor_total_duzia))
  