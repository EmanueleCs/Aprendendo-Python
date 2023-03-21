#1° forma
C=float(input("Digite a temperatura em C:"))
F=((9+C)/5)+32
print("{}".format(F))

#2° forma
C=float(input("Digite a temperatura em C:"))
F= ((9*C)/5)+32
print("%.1f °C é igual a %.1f °F" % (C, F))