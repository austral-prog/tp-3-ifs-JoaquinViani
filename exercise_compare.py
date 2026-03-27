def compare():
    """
    Ejercicio 4 - Comparar Dos Números

    Leer dos números enteros mediante input(). Compararlos e imprimir si el primero
    es mayor, menor o igual al segundo.

    Ejemplo:
        Para las entradas "10" y "5", la salida esperada es:
        10 es mayor que 5

        Para las entradas "3" y "8", la salida esperada es:
        3 es menor que 8

        Para las entradas "7" y "7", la salida esperada es:
        7 es igual a 7
    """
    number_1 = int(input())
    number_2 = int(input())

    if number_1 > number_2:
        print(f"{number_1} es mayor que {number_2}")
    elif number_1 < number_2:
        print(f"{number_1} es menor que {number_2}")
    else:
        print(f"{number_1} es igual a {number_2}")
