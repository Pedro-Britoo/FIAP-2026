digitesalario = int(input("digite seu salario em numeros inteiros"))
sujo = input("seu nome esta sujo? (sim o nao): ")
nomelimpo = bool()

if sujo == "sim":
    nomelimpo = False
else:
    if sujo == "nao":
        nomelimpo = True

if digitesalario >= 2000 and nomelimpo == True:
    print("nome limpo")
else:
    print("nome sujo")