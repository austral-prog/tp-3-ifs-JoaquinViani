def discount():
    precio = float(input())
    cantidad = int(input())

    subtotal = precio * cantidad

    if cantidad >= 10:
        descuento = 0.20
        porcentaje = "20%"
    elif cantidad >= 5:
        descuento = 0.10
        porcentaje = "10%"
    else:
        descuento = 0.0
        porcentaje = "0%"

    monto_descuento = subtotal * descuento
    total = subtotal - monto_descuento

    print(f"Subtotal: {subtotal}")
    print(f"Descuento aplicado: {porcentaje}")
    print(f"Monto de descuento: {monto_descuento}")
    print(f"Total final: {total}")
