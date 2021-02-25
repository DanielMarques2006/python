doente = input("está doente? ")

if doente == "sim":
    causa = input("a causa é conhecida? ")
    if causa == "sim":
        causa = input("qual a causa? ")
        if causa == "comida estragada":
            print("medicação: Zinco-Pro ou Flora 5 ")
        elif causa == "não tomar banho":
            print("medicação: hidratação e banhos frios")
        elif causa == "falta de ferro":
            print("medicação: suplomentos de ferro")
        elif causa == "picada de mosquito com malaria":
            print("medicação: cloroquina")
        elif causa == "picada de mosquito com febre amarela":
            print("medicação: repouso e hidratação")
        else:
            print("resposta inválida")
    elif causa == "não":
        sintomas = input("quais os sintomas? ")
        if sintomas == "diarreia e vómito":
            print("possivel causa: ingerir comida estragada")
            print("medicação: Zinco-Pro ou Flora 5 ")
        elif sintomas == "comixão e pele seca":
            print("possivel causa: não tomar banho")
            print("medicação: hidratação e banhos frios")
        elif sintomas == "diminuição de globlos vermelhos e hemacias":
            print("possivel causa: falta de ferro no sangue")
            print("medicação: suplomentos de ferro")
        elif sintomas == "febre, fraquza e cafaleia":
            print("possivel causa: picada de mosquito com malaria")
            print("medicação: cloroquina")
        elif sintomas == "febre, doe muscular e nausea":
            print("possivel causa: picada de mosquito com febre amarela")
            print("medicação: repouso e hidratação")
        else:
            print("resposta inválida")

    else:
           print("resposta inválida")      
elif doente == "não":
    print("ainda bem")

else:
    print("resposta inválida")
