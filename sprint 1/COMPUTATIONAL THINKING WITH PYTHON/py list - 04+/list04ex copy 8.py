nume1= int(input("Digite seu mes: "))

match nume1:
    case 1 | 2| 3 :
        print("1 trimestre") 
    case 4 | 5| 6 :
        print("2 trimestre") 
    case 7 | 8| 9 :
        print("3 trimestre") 
    case 10 | 11| 12 :
        print("4 trimestre") 
    case _:
        print("mes invalido")

