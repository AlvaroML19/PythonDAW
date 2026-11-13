c: int = int(input("Céntimos: "))
for valor in (50, 20, 10, 5, 2, 1):
    print(f"{valor}c: {c // valor}")
    c = c % valor