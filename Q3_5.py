p = 0
n = int(input("Digite um numero "))
for i in range(n+1):
    if i != 0 and n % i == 0:
        p += 1

if p == 2:
    print("Primo")
else:
    print("Não primo")