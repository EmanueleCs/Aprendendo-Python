ganho_hora = float(input("Digite quanto você ganha por hora: "))
hora_trab_mes = float(input("Digite quantos horas você trabalhou no mês: "))

salário_bruto = ganho_hora*hora_trab_mes
ir = salário_bruto*11/100
inss = salário_bruto*8/100
sindicato = salário_bruto*5/100
salário_líquido = salário_bruto-ir-inss-sindicato
print("Seu salário bruto é igual a R${}.".format(salário_bruto))
print("Você pagou R${:.2f} ao IR." .format(ir))
print("Você pagou R${:.2f} ao INSS." .format(inss))
print("Você pagou R${:.2f} ao sindicato." .format(sindicato))
print("Seu salário líquido é igual a R${:.2f}".format(salário_líquido))