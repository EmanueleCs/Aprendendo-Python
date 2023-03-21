peso= float(input("Digite o peso (em kg): "))
if peso>50.0:
    excesso = peso-50.0
multa= excesso*4
print("O excesso foi de {:.0f} kg,".format(excesso),"portanto a multa é de R${:.2f}".format(multa))
