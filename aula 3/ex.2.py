d=int(input("Digite a quantia de dia:"))
h=int(input("Digite a quantia de horas:"))
m=int(input("Digite a quantia de minutos:"))

segundos = d+86400+h*3600+m*60

print("{} dias, {} horas e {} minutos tem {} segundos".format(d, h, m, segundos))
#posso tbm substituir o "segundo" pela conta