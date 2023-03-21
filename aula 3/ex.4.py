km=int(input("Quantos km foram percorridos?"))
dias=int(input("Por quantos dias o carro foi alugado?"))
preço= 68*dias+0.15*km

print("R${:.2f} é o valor a ser pago".format(preço))