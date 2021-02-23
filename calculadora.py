x = float(input("insira o primeiro numero: "))
y = float(input("insira o segundo numero numero: "))
operacao = input("insira a operação desejada: ")



if operacao == "soma" or operacao == "+":
    print("A soma de ", x, "e ", y, "é igual a ", x + y)

elif operacao == "subtração" or operacao == "-":
    print("A subtração de ", x, "e ", y, "é igual a ", x - y)


elif operacao == "multiplicação" or operacao == "*":
    print("A multiplicação de ", x, "e ", y, "é igual a ", x * y)

elif operacao == "divisão" or operacao == "/":
    print("A divisão de ", x, "e ", y, "é igual a ", x / y)

else:
    print("Resposta invalida")

