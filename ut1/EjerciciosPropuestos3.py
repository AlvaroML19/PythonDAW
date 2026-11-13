total: int = int(input("Cuantos segundos has tardado en dar la vuelta: "))

horas = total / 3600
minutos = (total % 3600) // 60
segundos = total % 60

print(f"Has tardado {horas}h {minutos}m {segundos}s")