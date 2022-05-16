#Escreva um programa que receba 3 números inteiros como entrada e possa informar qual é o MAIOR.


n1= int(input("1º número: "))
n2= int(input("2º número: "))
n3= int(input("3º número: "))

maior_num = 0

if n1 > n2 and n1 > n3:
  print (n1)
if n2 > n1 and n2 > n3:
  print (n2)
if n3 > n1 and n3 > n2:
  print (n3)

"""
if n1 > maior_num:
  maior_num = n1
if n2 > maior_num:
  maior_num = n2
if n3 > maior_num:
  maior_num = n3

print (maior_num)
"""