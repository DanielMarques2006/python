a = float(input("indique o salário de Janeiro: "))
b = float(input("indique o salário de Fevereiro: "))
c = float(input("indique o salário de Março: "))
d = float(input("indique o salário de Abril: "))
e = float(input("indique o salário de Maio: "))
f = float(input("indique o salário de Junho: "))
g = float(input("indique o salário de Julho: "))
h = float(input("indique o salário de Agosto: "))
i = float(input("indique o salário de Setembro: "))
j = float(input("indique o salário de Outubro: "))
k = float(input("indique o salário de Novembro: "))
l = float(input("indique o salário de Dezembro: "))

print("A sua média salárial é de ", (a + b + c + d + e + f + g + h + i + j + k + l) / 12)

lista = [a, b, c, d, e, f, g, h, i, j, k, l]
print(min(lista))
print(max(lista))
