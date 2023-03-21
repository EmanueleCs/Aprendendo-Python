#Uso de marcadores
cidade="Campinas"
tempo_cidade=7
trabalho="São Roque"
tempo_trabalho=1.1
print("Eu moro em %s há %2d anos e trabalho em %2s há %.2f anos" % (cidade, tempo_cidade, trabalho, tempo_trabalho))

print("%-2d, %2.2f" % (tempo_cidade, tempo_trabalho)) #- depois do texto
print("%2s, %s" % (cidade, trabalho))


cidade="Campinas"
tempo_cidade=7
trabalho="São Roque"
tempo_trabalho=1.1
print("Eu moro em {2} há {1} e trabalho em {0} há {3} anos" .format(cidade, tempo_cidade, trabalho,tempo_trabalho))

cidade="Campinas"
tempo_cidade=7
trabalho="São Roque"
tempo_trabalho=1.1
print("Eu moro em {} há {:2d} e trabalho em {} há {:.2f} anos" .format (cidade, tempo_cidade, trabalho, tempo_trabalho))