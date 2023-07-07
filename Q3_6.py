p = 0
nd = []
n = int(input("Digite um numero "))
for i in range(n+1):
    if i != 0 and n % i == 0:
        p += 1
        nd.append(i)

if p == 2:
    print("Primo")
else:
    print("Não primo")
    print(f"Numeros divisiveis = {nd}")