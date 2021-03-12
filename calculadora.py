import math

x = float(input("insira o primeiro numero: "))
operacao = input("insira a operação desejada: ")


if operacao == "raiz quadrada":
    z = math.sqrt(x)
    print("A raiz quadrada de ", x, "é igual a ", z)
else:
    y = float(input("insira o segundo numero: "))

if operacao == "soma" or operacao == "+":
    print("A soma de ", x, "e ", y, "é igual a ", x + y)

elif operacao == "subtração" or operacao == "-":
    print("A subtração de ", x, "e ", y, "é igual a ", x - y)


elif operacao == "multiplicação" or operacao == "*":
    print("A multiplicação de ", x, "e ", y, "é igual a ", x * y)

elif operacao == "divisão" or operacao == "/":
    print("A divisão de ", x, "e ", y, "é igual a ", x / y)

elif operacao == "potencia":
    print(x, "elevado a ", y, "é", x ** y)

