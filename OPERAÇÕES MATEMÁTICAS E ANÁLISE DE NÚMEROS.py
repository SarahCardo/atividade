num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Não é possível dividir por zero"
print("\n--- Operações ---")
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("\n--- Analisando o primeiro número ---")
if num1 % 2 == 0:
    print(num1, "é par")
else:
    print(num1, "é ímpar")
contador = 0
for i in range(1, num1 + 1):
    if num1 % i == 0:
        contador += 1
if contador == 2:
    print(num1, "é primo")
else:
    print(num1, "não é primo")
print("\n--- Analisando o segundo número ---")
if num2 % 2 == 0:
    print(num2, "é par")
else:
    print(num2, "é ímpar")
contador = 0
for i in range(1, num2 + 1):
    if num2 % i == 0:
        contador += 1
if contador == 2:
    print(num2, "é primo")
else:
    print(num2, "não é primo")
    