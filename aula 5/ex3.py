#imc = peso/(altura)²
#abaixo 18,5 abaxo
#entre 18,5 e 25 normal
#entre 25 e 30 acima
#acima 30 obeso

peso= float(input("Digite seu peso:"))
altura= float(input("Digite sua altura:"))

imc= peso/(altura)**2

if (imc <18.5):
    print ("Você está abaixo do peso.")
elif (imc >=18.5 and imc <25):
    print ("Seu peso está normal.")
elif (imc >=25 and imc <=30):
    print ("Você está acima do peso.")
elif (imc > 30):
    print ("Você está obeso.")
