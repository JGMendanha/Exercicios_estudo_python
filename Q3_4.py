p = 0
im = 0
for i in range(10):
    n = int(input("Digite um numero "))
    if n % 2 == 0:
        p += 1
    else:
        im += 1
    
print(f"Quantida de numeros pares = {p}\nQuantidade de numeros impares = {im}")
