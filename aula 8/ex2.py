import random # módulo random
numero = random.randrange(1,101) #numero entre 1 e 100

teste = int(input("Digite um numero:"))
tentativa = 1

if teste== numero:
    print("Acertou!!!")
else:
    while teste != numero:
        if teste < numero:
            print("Foi abaixo.")
        else:
            print("Foi acima.")
        teste = int(input("Digite um numero: "))
        tentativa = tentativa + 1
        if teste == numero:
            print("Acertou em", tentativa, "tentativa(s)!!!")