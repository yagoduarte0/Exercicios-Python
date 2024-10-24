quantidade = 0

for i in range(5):
    valor = int(input())
    if valor % 2 == 0:
        quantidade = quantidade + 1

print(f"{quantidade} valores pares")