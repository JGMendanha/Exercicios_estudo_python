a = []
b = []
c = []
d = []
e = []
while(True):
    n = float(input("Digite uma nota "))
    if n == -1:
        break
    if n >= 9 and n <= 10:
        a.append(n)
    elif n >= 8 and n < 9:
        b.append(n)
    elif n >= 7 and n < 8:
        c.append(n)
    elif n >= 6 and n < 7:
        d.append(n)
    elif n >= 0 and n < 6:
        e.append(n)

print(f"Notas conceito A = {a}\nNotas conceito B = {b}\nNotas conceito C = {c}\nNotas conceito D = {d}\nNotas conceito E = {e}\n")