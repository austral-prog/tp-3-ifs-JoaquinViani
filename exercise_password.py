def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    pwd = input()

    if len(pwd) < 8:
        print("Contraseña muy corta")

    if "0" not in pwd and "1" not in pwd and "2" not in pwd and "3" not in pwd and "4" not in pwd and "5" not in pwd and "6" not in pwd and "7" not in pwd and "8" not in pwd and "9" not in pwd:
        print("Debe contener un numero")

    if len(pwd) >= 8 and ("0" in pwd or "1" in pwd or "2" in pwd or "3" in pwd or "4" in pwd or "5" in pwd or "6" in pwd or "7" in pwd or "8" in pwd or "9" in pwd):
        print("Contraseña valida")

