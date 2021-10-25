n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

op = int(input("Digite 1 - Soma ou 2 - Subtração: "))

if(op == 1):
    soma = n1 + n2
    print(f"{n1} + {n2} = {soma}")

elif(op == 2):
    sub = n1 - n2
    print(f"{n1} - {n2} = {sub}")

else:
    print("Erro, Digite uma opção valida!")
    exit()