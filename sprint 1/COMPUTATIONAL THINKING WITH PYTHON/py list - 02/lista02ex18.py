senhaconta = int(input("coloque a senha da conta e 12345 "))
conta_bloqueada = False

if senhaconta == 12345:
    conta_bloqueada = False
else:
    conta_bloqueada = True

if not conta_bloqueada:
    print("Conta ativa")
else:
    print("Conta bloqueada")