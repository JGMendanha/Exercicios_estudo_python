s = float(input("Digite seu salario "))

if s < 1903.98:
    print("Isento")
elif s > 1903.98 and s < 2826.65:
    ip = s * 0.075 + 143.80
    print(f"Imposto = {ip}")
elif s > 2826.65 and s < 3751.05:
    ip = s * 0.15 + 354.80
    print(f"Imposto = {ip}")
elif s > 3751.05 and s < 4664.69:
    ip = s * 0.225 + 636.13
    print(f"Imposto = {ip}")
elif s > 4664.68:
    ip = s * 0.275 + 869.36
    print(f"Imposto = {ip}")