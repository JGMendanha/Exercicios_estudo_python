def seg(d, h, m, s):
    soma = 0
    soma += s
    soma += (m * 60)
    soma += (h * 3600)
    soma += (d * 86400)
    return soma

d = int(input("Digite o numero de dias "))
h = int(input("Digite o numero de horas "))
m = int(input("Digite o numero de minutos "))
s = int(input("Digite o numero de segundos "))
print(f"Numero de segundos em {d} dias {h} horas {m} minutos e {s} segundos = {seg(d,h,m,s)}")