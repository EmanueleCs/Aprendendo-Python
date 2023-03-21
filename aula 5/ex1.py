altura=float(input("Digite seu sexo (M ou F"))
sexo= str(input())

if (sexo == "M"):
    print("Seu peso ideal é {:.2f}kg." .format((72.7*altura)-58))
elif (sexo == "F"):
    print("Seu peso ideal é {:.2f}kg." .format((62.1*altura)-44.7))