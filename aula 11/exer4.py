lista = []
palavra = str(input("Digite um palavra:"))

while palavra.isalpha():
   lista.append(palavra)
   palavra = str(input("Digite um palavra:"))

print("{} = {} palavras".format(sorted(lista), len(lista)))
