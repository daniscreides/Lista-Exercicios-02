#Escreva um algoritmo para ler um número inteiro e exiba se ele é maior, igual ou menor que zero.

numero = int(input("Digite o número: "))

if numero > 0:
  print ("Esse número é maior que 0")
elif numero < 0:
  print ("Esse número é menor que 0")
else:
  print ("Esse número é igual a 0")