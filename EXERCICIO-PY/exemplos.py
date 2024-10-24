def dobra(y):
    global x
    x = y + y
    return x

x = 5
dobra(x)
dobra(x)
print(x)

def dobra(y):
    x = y + y
    return x

x = 5
dobra(x)
dobra(x)
print(x)

print(8.5 / 2 // 2)

valor = input("Informe um valor: ")
print(not int(valor) % 2)

x = 2
y = 10
z = -2

print(x % (3 + y) * x - z ** 2)