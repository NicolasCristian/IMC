

peso = float(input('digite seu peso'))
print (peso)
alt = float(input('agora digite sua altura'))
print (alt)
imc = peso / (alt ** 2)
print ('o seu imc e de:{:.1f}'.format (imc))

if imc < 18.5:
  print ("voce esta abaixo do peso normal")
elif 18.5 <= imc < 25:
  print ("voce esta com o peso normal")
elif 25 <= imc < 30:
  print ("voce esta com o peso um pouco acima do normal")
elif 30 <= imc < 35:
  print ("voce esta com obesidade grau I")  
elif 35 <= imc < 39.5:
  print ("voce esta com obesidade grau II")  
elif 40 >= imc:
  print ("voce esta com obesidade grau III")