#spacex sai primeiro
D1 = int(input()) #distância entre terra e marte lançamento spacex
V1 = int(input()) #velocidade spacex
T = int(input()) #tempo em dias entre o lançamento de um e da outra
D2 = int(input()) #distância entre terra e marte lançamento blueorigin
V2 = int(input()) #velocidade blueorigin


if ((D1/V1)/24<((D2/V2)/24)+T):
    print(True)
else:
    print(False)

#t=vm/d
#subtrai o t ao fi