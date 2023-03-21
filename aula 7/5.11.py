deposito=int(input())
taxa=int(input())
rendimento=deposito+(deposito*taxa/100)

for i in range (25):
    print("R${:.2f}".format(rendimento))
    rendimento= rendimento+(rendimento*taxa/100)