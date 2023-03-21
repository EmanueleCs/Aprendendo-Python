#3.10
salário = int(input("Digite seu salário:"))
porcentagem = int(input("Digite sua porcentagem de aumento:"))
aumento=salário*porcentagem/100
salário=salário+aumento
print("Você teve um aumento de", aumento, "portanto seu novo salário é de", salário)