deposito=int(input())
taxa=int(input())
mes=1
rendimento=deposito+(deposito*taxa/100)

for i in range (mes,24):
    print("R${:.2f}".format(rendimento))
    nvdep = int(input("Digite o valor do novo depósito:"))
    rendimento= rendimento+nvdep+(rendimento+nvdep*taxa/100)