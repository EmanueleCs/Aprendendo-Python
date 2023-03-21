metros_quadrados = float(input())

litros=(metros_quadrados/3)
latas= litros/18
preço= latas*80

print("Você deve comprar {:.1f} latas de tinta, tendo como preço total R${:.1f}.".format(latas, preço))