salario = float(input())
percentual = 0

if salario <= 400.0:
    percentual = 15
elif salario <= 800.0:
    percentual = 12
elif salario <= 1200.0:
    percentual = 10
elif salario <= 2000.0:
    percentual = 7
else:
    percentual = 4

reajuste = salario * percentual/100
salarioNovo = salario + reajuste

print(f"Novo salario: {salarioNovo:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")