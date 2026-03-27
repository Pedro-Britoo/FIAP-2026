nume1 = int(input("digite o codigo: "))

match nume1:
    case 1 | 2:
        print("alimentos")
    case 3 | 4:
        print("limpeza")
    case 5 | 6:
        print("higiene")
    case _:
        print("codigo invalido")