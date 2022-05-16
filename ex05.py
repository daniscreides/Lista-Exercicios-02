#Faça um programa que leia o nome do eleitor e sua idade e seja capaz de informar sua classe eleitoral, de acordo com as instruções abaixo:
#Não eleitor (abaixo de 16 anos);
#Eleitor obrigatório (entre 18 e 65 anos) e
#Eleitor facultativo (16, 17 anos ou acima dos 65 anos).

"""if idade < 16:
  print ("Não eleitor!")
else:
  if idade < 18 or idade > 65: 
    print ("Eleitor facultativo")
  else:
    print ("Eleitor Obrigatório!")
"""


nome = input("Nome: ")
idade = int (input("Idade: "))

if idade < 16:
  print ("Não eleitor!")
elif idade >= 16 and idade < 18:
  print ("Eleitor facultativo.")
elif idade >= 18 and idade < 65:
  print ("Eleitor obrigatório.")
else:
  print ("Eleitor facultativo.")
