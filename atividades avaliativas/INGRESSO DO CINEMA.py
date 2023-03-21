#elif dia==2:
#    if hora<=18 and minuto<=30:
#        if estudante =="S":
#            print("Valor do ingresso: R${}".format(15*0.5))
#        elif pagamento == "C":
#            print("Valor do ingresso: R${}".format(15*0.5))
#        else:
#            print("Valor do ingresso: R${}".format(15))
#    elif hora>=18 and minuto>30:
#        if estudante =="S":
#            print("Valor do ingresso: R${}".format(20*0.5))
#        elif pagamento == "C":
#            print("Valor do ingresso: R${}".format(20*0.5))
#        else:
#            print("Valor do ingresso: R${}".format(20))

dia= int(input())
hora= int(input())
minuto= int(input())
estudante= str(input())
pagamento= str(input())


if dia==1:
    if hora<=18 and minuto<=30:
        if estudante =="S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(30 * 0.5))
        elif estudante =="N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(30 * 0.3))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(30))
    elif hora>=18 and minuto>30:
        if estudante == "S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(30 * 0.5))
        elif estudante == "N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(30 * 0.3))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(30))
elif dia==2:
    if hora<=18 and minuto<=30:
        if estudante =="S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(15 * 0.5))
        elif estudante =="N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(15 * 0.5))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(15))
    elif hora>=18 and minuto>30:
        if estudante == "S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(20*0.5))
        elif estudante == "N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(20 * 0.5))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(20))
elif dia==3:
    if hora<=18 and minuto<=30:
        if estudante =="S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(15 * 0.5))
        elif estudante =="N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(15 * 0.5))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(15))
    elif hora>=18 and minuto>30:
        if estudante == "S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(20 * 0.5))
        elif estudante == "N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(20 * 0.5))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(20))
elif dia==4:
    if hora<=18 and minuto<=30:
        if estudante =="S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(15 * 0.5))
        elif estudante =="N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(15 * 0.5))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(15))
    elif hora>=18 and minuto>30:
        if estudante == "S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(30 * 0.5))
        elif estudante == "N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(30 * 0.5))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(30))
elif dia==5:
    if hora<=18 and minuto<=30:
        if estudante =="S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(20 * 0.5))
        elif estudante =="N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(20 * 0.5))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(20))
    elif hora>=18 and minuto>30:
        if estudante == "S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(30 * 0.5))
        elif estudante == "N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(30 * 0.5))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(30))
elif dia==6:
    if hora<=18 and minuto<=30:
        if estudante =="S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(20 * 0.5))
        elif estudante =="N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(20 * 0.5))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(20))
    elif hora>=18 and minuto>30:
        if estudante == "S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(40 * 0.5))
        elif estudante == "N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(40 * 0.3))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(40))
if dia==6:
    if hora<=18 and minuto<=30:
        if estudante =="S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(30 * 0.5))
        elif estudante =="N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(30 * 0.2))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(30))
    elif hora>=18 and minuto>30:
        if estudante == "S":
            if pagamento == "D" or pagamento == "C":
                print("Valor do ingresso: R${}".format(40 * 0.5))
        elif estudante == "N":
            if pagamento == "C":
                print("Valor do ingresso: R${}".format(40 * 0.2))
            elif pagamento == "D":
                print("Valor do ingresso: R${}".format(40))