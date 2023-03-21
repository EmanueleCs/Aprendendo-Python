dep= float(input("Digite o valor inicial:"))
taxa= float(input("Dgite o valor da taxa:"))
mes=1
valor_final= dep

while(mes<=24):
    print(("Valor no {}° mês: {:.2f} mês".format (mes,valor_final)))
    valor_final=(valor_final + (valor_final * taxa / 100))
    mes=mes+1