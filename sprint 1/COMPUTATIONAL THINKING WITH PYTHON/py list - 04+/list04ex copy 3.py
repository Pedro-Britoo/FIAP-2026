turno = (input("coloque a letra do turno "))

match turno.lower:
    case "m" :
        print("Bom dia")
    case "t" :
        print("Boa tarde")
    case "m" :
        print("Boa noite")
    case _:
            print("Turno invalido")