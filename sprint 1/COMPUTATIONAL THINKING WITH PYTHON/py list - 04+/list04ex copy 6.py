numero1 = int(input("digite um numero"))
numero2 = int(input("digite um numero"))
operacao = (input("digite uma operacao"))

match operacao:
    case "+" :
        resultado = numero1 * numero2
        print(resultado)
    case "-" :
        resultado = numero1 - numero2
        print(resultado)
    case "/" :
        resultado = numero1 / numero2
        print(resultado)
    case "*" :
        resultado = numero1 * numero2
        print(resultado)
        
        
        
