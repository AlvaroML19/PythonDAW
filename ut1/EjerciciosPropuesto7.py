def linea_ticket(producto: str, unidades: int, precio: float) -> str:
    importe: float = precio * unidades
    return f"{producto:<12}{unidades:>3} x {precio:>6.2f} = {importe:>8.2f} €"

print(linea_ticket("Zapatos",5,6))