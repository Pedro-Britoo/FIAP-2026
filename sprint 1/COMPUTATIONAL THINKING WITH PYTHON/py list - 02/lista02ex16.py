idade = int(input("coloque sua idade"))

concluiumedio = input("voce concluiu o medio?")
terminouensinomedio = bool()

if concluiumedio == "sim" :
    terminouensinomedio == True
else:
    terminouensinomedio == False

if idade >= 18 and concluiumedio == True :
        print("voce terminou o ensino medio")
else:
    print("voce nao terminou o ensino medio")