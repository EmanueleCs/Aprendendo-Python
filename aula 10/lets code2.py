frase  = str(input())
caractere = input()
qtde = 0

for letra in frase:
    if letra == caractere:
        qtde = qtde+1

print ("O caractere ocorre {} vezes." .format(qtde))