"""O preço do Kw/h é aplicado de acordo com a quantidade de energia elétrica consumida, conforme pode-se ver na tabela abaixo:
CONSUMO MENSAL (CM)
PREÇO Kw/h (em R$)
CM  300
R$ 1.00
CM  200 e CM <300 
R$ 0.80
CM < 200
R$ 0.20


Faça um programa para receber o consumo mensal e depois calcular o total a pagar no mês. A saída do sistema deve ter o seguinte formato:
Consumidor: <FULANO>
Consumo mensal: <X>
Preço do kw/h em R$: <P>           
Total a pagar R$: <Y>
"""

consumidor = input("Consumidor: ")
consumo = float(input("Consumo mensal: "))
preco = 0 
total_pagar = 0

if consumo >= 300: 
  preco = 1.00
elif consumo >= 200 and consumo < 300:
  preco = 0.80
else:
  preco = 0.20

total_pagar = (consumo * preco)

print ("ENERGIA DO MÊS")
print ("Consumidor: " + consumidor)
print ("Consumo Mensal: " + str(consumo))
print ("Preço do kw/h R$ " + str(preco))        
print ("Total a pagar R$ " + str(total_pagar))
