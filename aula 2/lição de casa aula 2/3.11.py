#3.10
preço = int(input("Digite o preço da mercadoria:"))
percentual = int(input("Digite seu percentual de desconto:"))
desconto=preço*percentual/100
preço=preço-desconto
print("O valor do desconto é", desconto, "portanto o valor da mercadoria com desconto é", preço)