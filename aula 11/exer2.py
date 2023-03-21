lista = [] #0-25
lista1 = [] #26-50
lista2 = [] #51-75
lista3 = [] #76-100

num = float(input("Digite um número:"))

while num >= 0:
    if num > 0 and num <= 25:
        if num not in lista:
            lista.append(num)
    elif num > 25 and num <= 50:
        if num not in lista1:
            lista1.append(num)
    elif num > 50 and num <= 75:
        if num not in lista2:
            lista2.append(num)
    elif num > 75 and num <= 100:
        if num not in lista3:
            lista3.append(num)
    num = float(input("Digite um número:"))

print("[0-25] = {} com {} numero(s).".format(sorted(lista), len(lista)))
print("[26-50] = {} com {} numero(s).".format(sorted(lista1), len(lista1)))
print("[51-75] = {} com {} numero(s).".format(sorted(lista2), len(lista2)))
print("[76-100] = {} com {} numero(s).".format(sorted(lista3), len(lista3)))