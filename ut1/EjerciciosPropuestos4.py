descuento: int = 15
precio: float = float(input("Cuanto ha costado tu camiseta: "))

precio_final = precio - precio * descuento / 100

print(f"Las zapatillas con descuento se quedan en: {precio_final}")