#lista = [8.0, 5.5, 9.3, 7.6, 3.1]

#for i in range(4):
#    print(lista[i] + lista[i+1])

#for i in range(4):
#    print(lista[i])
#____________________________________________
#lista = []
#print(lista)
#lista.append(10)
#print(lista)
#lista.append(20)
#print(lista)

#print(len(lista))
#____________________________________________
quant= int(input("Entre com um número:"))
lista = []

for i in range(quant):
    elemento = float(input("Digite um elemento:"))
    lista.append(elemento)

print(lista)