frase = str(input())

for i in range(len(frase)-1, -1, -1):
    print (frase[i], end="")

print(frase[::-1])