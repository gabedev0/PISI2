N = int(input("Numeros de peças: "))
P = input("Digite as peças:")

lista_P = P.split()
total_P = 0

for numero in lista_P:
    total_P += int(numero)

total_N = (N + 1) * N // 2

peca_F = total_N - total_P
print(peca_F)
