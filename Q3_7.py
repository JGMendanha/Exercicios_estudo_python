
n = int(input("Digite um numero "))
m = n

for i in range(n):
    print("*", end=" ")

print("\n", end="")

for i in range(n-2):
    for j in range(n):
        if j == 0 or j == (m-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print("\n", end="") 

for i in range(n):
    print("*", end=" ")