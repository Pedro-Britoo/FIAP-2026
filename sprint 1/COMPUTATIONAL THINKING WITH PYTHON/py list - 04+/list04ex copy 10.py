valor = int(input("digite o valor da compra"))
desconto = float(0.10)


resultado = valor * (1 - desconto) if valor > 100 else valor

print("Valor final:", resultado)