produto= float(input("Digite o código do produto:"))

if (produto==1):
    print ("Alimento não perecível")
elif (produto==2 or produto==3 or produto==4):
    print ("Alimento perecível")
elif (produto==5 or produto==6):
    print ("Vestuário")
elif (produto== 7):
    print("Higiene pessoal")
elif (produto >= 8 and produto <=15):
    print ("Limpeza e utensílios domésticos")
else:
    print("Inválido")