# Documentación para el código

El siguiente código en Python crea una matriz de tamaño `tam` y permite al usuario ingresar datos en ella hasta que se ingrese la palabra "fin". 

```python
tam = 5  # Define el tamaño de la matriz
~~t = tam - 1  # Variable auxiliar~~
matriz = [None] * tam  # Crea una matriz de tamaño 'tam' con todos los elementos inicializados en None
i = 0  # Índice para recorrer la matriz

# Bucle que se ejecuta hasta que se llena la matriz
while i < tam:
    print(matriz)  # Imprime el estado actual de la matriz
    dto = input("Ingrese un dato: ")  # Solicita al usuario un dato para agregar a la matriz
    if dto == "fin":  # Si el usuario ingresa 'fin', se termina el bucle
        break
    print(f"i: {i}")  # Imprime el índice actual
    if matriz[i] != 0:  # Si el elemento en el índice actual de la matriz no es 0, se agrega el dato ingresado por el usuario
        print(f"Se agrego el dato {dto} en la posicion {i} con el valor {matriz[i]}")  # Imprime un mensaje indicando que se agregó el dato
        matriz[i] = dto  # Agrega el dato en el índice actual de la matriz
        i += 1  # Incrementa el índice
        if i == tam:  # Si el índice es igual al tamaño de la matriz, se reinicia a 0
            i = 0