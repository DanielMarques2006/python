# Estes é uma nova alteração do mi

salario = float(input("Digite o seu salário: "))
despesas = float(input("Digite o valor das suas despesas: "))
lucro = salario - despesas

if lucro >= 0:
    print("O deu lucro é de: ", lucro)
else:
    print("O seu prejuizo é de: ", abs(lucro))  