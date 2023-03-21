salário= float(input("Digite seu salário: "))

if(salário<=1250):
    print("Você receberá aumento no valor de R${:.2f}.".format(salário*15/100))
else:
    print("Você recebrá aumento no valor de R${:.2f}.".format(salário*10/100))