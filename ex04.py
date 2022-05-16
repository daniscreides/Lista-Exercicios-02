"""" Escreva um programa para uma clínica médica que determine o grau de obesidade de uma pessoa. Devem ser fornecidos como entrada o peso (em kilogramas) e a altura (em metros) da pessoa. O grau de obesidade é determinado pelo IMC – Índice de Massa Corpórea (IMC = Peso / Altura2). No final, o programa deve emitir as mensagens correspondentes conforme a tabela a seguir:
Valor do IMC
Mensagem do sistema
Abaixo de 18.5
Você está abaixo do seu peso ideal
Entre 18.5 e 24.9
Parabéns! Você está no seu peso ideal!
Entre 25.0 e 29.9
Você está acima do seu peso (sobrepeso)
Entre 30.0 e 34.9
Obesidade grau I
Entre 35.0 e 39.9
Obesidade grau II
Acima de 40.0
Obsesidade grau III """



peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = (peso/altura**2)

if imc < 18.5:
  print ("Você está abaixo do seu peso ideal.")
elif imc >= 18.5 and imc <= 24.9:
  print ("Parabéns! Você está no seu peso ideal!")
elif imc >= 25.0 and imc <= 29.9:
  print ("Você está acima do seu peso.(sobrepeso) ")
elif imc >= 30.0 and imc <= 34.9:
  print ("Obesidade I") 
elif imc >= 35.0 and imc <= 39.9:
  print ("Obesidade II")
else: 
  print ("Obesidade III")