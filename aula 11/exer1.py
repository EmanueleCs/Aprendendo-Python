lista = []
resposta = "S"
soma = 0

while resposta == "S":
    valor = float(input("Digite um elemento:"))
    soma = soma + valor
    lista.append(valor)
    resposta = input("Quer continuar? [S/N]").upper()
print(lista)
print("A média é: {:.2f}" .format(soma/len(lista)))