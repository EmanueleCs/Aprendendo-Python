numero= int(input("Digite um número: "))

if(numero<100 and numero%2==0):
    print("Este n° é par e menor que 100.")
if(numero>100 and numero%2==0):
    print("Este n° é par e maior que 100.")
if(numero>100 and numero%2!=0):
    print("Este n° é ímpar e maior que 100.")
if(numero<100 and numero%2!=0):
    print("Este n° é ímpar e menor que 100.")

