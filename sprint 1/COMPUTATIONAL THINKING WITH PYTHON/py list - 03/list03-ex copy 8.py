numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))

operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
    print("Resultado:", resultado)

elif operacao == "-":
    resultado = numero1 - numero2
    print("Resultado:", resultado)

elif operacao == "*":
    resultado = numero1 * numero2
    print("Resultado:", resultado)

elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    else:
        print("Erro: divisão por zero")

else:
    print("Operação inválida")