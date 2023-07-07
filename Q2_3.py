l = float(input("Digite a quantidade de litros "))
tp = str(input("Digite se deseja gasolina (G) ou alcool (A) "))

if tp == "A":
    if l < 20:
        d = 2.80 * 0.97
        p = d * l
        print(f"Total a pagar = {p}")

    elif l > 20:
        d = 2.80 * 0.95
        p = d * l
        print(f"Total a pagar = {p}")

elif tp == "G":
    if l < 20:
        d = 4.20 * 0.96
        p = d * l
        print(f"Total a pagar = {p}")

    elif l > 20:
        d = 4.20 * 0.94
        p = d * l
        print(f"Total a pagar = {p}")