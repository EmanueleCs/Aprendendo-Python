velocidade =float(input("Digite a velocidade do carro: "))

if(velocidade>80):
    print("Você foi multado no valor de R${:.2f}.".format((velocidade-80)*5))
else:
    print("Você não foi multado, continue seu caminho.")