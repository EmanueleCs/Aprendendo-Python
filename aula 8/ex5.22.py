operação=input("Digite a operação (A, S, D ou M):")

while operação!= "sair":
    if operação=="A":
        for i in range(1,11):
            print("TABUADA DO {}".format(i))
            for j in range(1,11):
                print ("{} + {} = {}".format(i,j, i+j))
    elif operação=="S":
        for i in range(1,11):
            print("TABUADA DO {}".format(i))
            for j in range(1,11):
                print ("{} + {} = {}".format(i,j, i-j))
    elif operação=="D":
        for i in range(1,11):
            print("TABUADA DO {}".format(i))
            for j in range(1,11):
                print ("{} + {} = {}".format(i,j, i/j))
    elif operação=="M":
        for i in range(1,11):
            print("TABUADA DO {}".format(i))
            for j in range(1,11):
                print ("{} + {} = {}".format(i,j, i*j))
    operação = input("Digite a operação (A, S, D ou M):")
else:
    print("Acabou!")