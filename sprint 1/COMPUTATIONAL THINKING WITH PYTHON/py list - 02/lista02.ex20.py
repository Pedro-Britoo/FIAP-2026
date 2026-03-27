idade = int(input("qual sua idade: "))
autorizacao = input("voce tem autorizacao sim ou nao ")

if idade >= 12 and idade <= 16 and autorizacao == "sim":
    print("acesso liberado")
else:
    print("acesso negado")