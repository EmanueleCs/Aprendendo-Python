resposta=input("Quer realizar o cálculo?")

while resposta=="S" or resposta=="s" or resposta=="sim" or resposta=="Sim":
    genero = input("Você F ou M?")
    altura = float(input("Digite sua altura:"))
    if genero=="M" or genero=="m":
        print("Seu peso ideal é: {:.2f}kg" .format((62.1*altura)-44.7))
    elif genero=="H" or genero=="h":
        print("Seu peso ideal é: {:.2f}kg" .format((72*altura)-58))
    resposta = input("Quer realizar o cálculo?")