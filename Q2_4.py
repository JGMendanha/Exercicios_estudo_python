while(True):
    s = float(input("Digite o valor do saque (Valores acima de 10 reais, multiplos de 10 e ate 1000 reais) "))
    if s >= 10 and s % 10 == 0 and s <= 1000:
        break

qdz = 0
qc = 0
qci = 0
qv = 0
qd = 0

while(s != 0):
    if s >= 200:
        s = s - 200
        qc += 1
    elif s >= 100:
        s = s - 100
        qc += 1
    elif s >= 50:
        s = s - 50
        qci += 1
    elif s >= 20:
        s = s - 20
        qv += 1
    elif s >= 10:
        s = s - 10
        qd += 1

print(f"Quantidade de notas de 200 = {qdz}\nQuantidade de notas de 100 = {qc}\nQuantidade de notas de 50 = {qci}\nQuantidade de notas de 20 = {qv}\nQuantidade de notas de 10 = {qd}\n")
