numero_de_comandos = input("numero_de_comandos")
lista = []
for i in range(0, int(numero_de_comandos)):
    comando = input(f" comando {i} : ")
    if "insert" in  comando:
        pedacos = comando.split(' ')
        index = int(pedacos[1])
        valor = int(pedacos[2])
        lista.insert(index, valor)
    elif "print" in  comando:
        print(lista)
    elif "remove" in  comando:
        pedacos = comando.split(' ')
        lista.remove(int(pedacos[1]))
    elif "append" in  comando:
        pedacos = comando.split(' ')
        lista.append(int(pedacos[1]))
    elif "sort" in  comando:
        lista.sort()
    elif "pop" in  comando:
        lista.pop()
    elif "reverse" in  comando:
        lista.reverse()
    
