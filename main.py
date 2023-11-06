tam = 5 
t = tam - 1
matriz = [None] * tam
i = 0
while i < tam:
    print(matriz)
    dto = input("Ingrese un dato: ")
    if dto == "fin":
        break
    print(f"i: {i}")
    if matriz[i] != 0:
        print(f"Se agrego el dato {dto} en la posicion {i} con el valor {matriz[i]}")
        matriz[i] = dto
        i += 1
        if i == tam:  # Si i es igual a tam, entonces lo reiniciamos a 0
            i = 0
