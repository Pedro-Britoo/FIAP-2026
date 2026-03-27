peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print("Abaixo do peso")

elif IMC < 25:
    print("Normal")

elif IMC < 30:
    print("Sobrepeso")

else:
    print("Obesidade")