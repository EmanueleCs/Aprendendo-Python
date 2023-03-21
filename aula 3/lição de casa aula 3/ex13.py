altura= float(input("Digite sua altura:"))
sexo= input("Você é homem ou mulher?")
if sexo=="homem":
    print("Seu peso ideal é {:.2f}" .format ((72.7*altura)-58))
elif sexo=="mulher":
    print("Seu peso ideal é {:.2f}".format ((62.1*altura)-44.7))