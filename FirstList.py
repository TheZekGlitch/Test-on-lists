lista = [type(123), type(1.1), type('cde'),type([])]
i = 0

while i < 4:
    print(lista[i])
    i += 1
del lista[2]
lista.append('final')

print(lista)
lista.pop()
print(lista)
