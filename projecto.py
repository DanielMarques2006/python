# Este é uma nova alteração

salario = float(input("Digite o seu salário: "))
despesas = float(input("Digite o valor das suas despesas: "))
lucro = salario - despesas

if lucro >= 0:
    print("O seu lucro é de: ", lucro)
else:
    print("O seu prejuizo é de: ", abs(lucro))  

print("O imapcto percentual das despesas sobre o salário é de ", despesas * 100 // salario, "%")