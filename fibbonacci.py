lista = []
#[0,1,1,2,3,5,8,13]

anterior = 0
atual = 1
lista.append(0)
lista.append(1)

for item in range(0,10):
    proximo = anterior + atual
    lista.append(proximo)
    anterior = atual
    atual = proximo
print(lista)
