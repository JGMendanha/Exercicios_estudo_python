n = int(input("Digite o valor de n "))
m = []
for i in range(n):
    m.append("*")
    for e in m:
        print(e, end=" ")
    print("\n", end="")